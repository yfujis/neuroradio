#!/usr/bin/env python3
"""Google Docs の原稿から新エピソードの投稿ファイルと画像フォルダを作る。

Google Docs で「ファイル → ダウンロード → ウェブページ (.html、zip)」を選び、
その zip (または展開したフォルダ / .html) を渡します。

使い方:
  python3 tools/new_episode.py ~/Downloads/116Dr._HammerfromU.zip
  python3 tools/new_episode.py "~/Desktop/#116 Dr. Hammer from U" --guests "長濱健一郎,小坂田拓哉"
  python3 tools/new_episode.py <zip> --date 2026-12-01 --dry-run
  python3 tools/new_episode.py --fill-links 116     # 配信後に Spotify / Apple の URL を埋める

オプション:
  --date YYYY-MM-DD   公開日 (省略時は今日)
  --slug Slug         URL 用の英数字名 (省略時は英語タイトルから自動生成)
  --guests 名前,名前    guests: に入れるゲストの実名 (Docs に「ゲスト名:」行があれば不要)
  --no-fetch          Spotify / Apple の URL を取りに行かない
  --dry-run           ファイルを書かずに、生成結果を表示するだけ
  --force             既存のファイルを上書きする
"""
from __future__ import annotations

import argparse
import datetime as dt
import html
import json
import re
import shutil
import sys
import tempfile
import unicodedata
import urllib.request
import xml.etree.ElementTree as ET
import zipfile
from dataclasses import dataclass, field
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import parse_qs, quote, urlparse

sys.dont_write_bytecode = True  # tools/__pycache__ を作らない
sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_posts  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
APPLE_PODCAST_ID = "1556937028"
RSS_URL = "https://anchor.fm/s/4ddf5488/podcast/rss"
USER_AGENT = "Mozilla/5.0 (compatible; neuroradio-tools)"

warnings: list[str] = []


def warn(msg: str) -> None:
    warnings.append(msg)


# --------------------------------------------------------------------------
# Google Docs HTML -> lines
# --------------------------------------------------------------------------

BLOCK_TAGS = {"p", "li", "h1", "h2", "h3", "h4", "h5", "h6"}


def unwrap_google_redirect(href: str) -> str:
    if re.match(r"^https?://www\.google\.[a-z.]+/url\?", href):
        q = parse_qs(urlparse(href).query).get("q")
        if q:
            return q[0]
    return href


@dataclass
class Block:
    tag: str
    pieces: list = field(default_factory=list)  # ("t", text) | ("a", text, href) | ("img", src) | ("br",)


class DocParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.blocks: list[Block] = []
        self.cur: Block | None = None
        self.skip_depth = 0
        self.href: str | None = None
        self.link_text = ""
        self.drop_anchor = False
        self.done = False  # reached the comments section at the end of the doc

    def handle_starttag(self, tag, attrs):
        if self.done:
            return
        a = dict(attrs)
        if tag in ("head", "style", "script", "title"):
            self.skip_depth += 1
            return
        if tag in BLOCK_TAGS:
            self._close_block()
            self.cur = Block(tag)
        elif tag == "a":
            href = a.get("href") or ""
            if href.startswith("#cmnt_ref"):
                self.done = True  # comment bodies start here
                self._close_block()
                return
            if href.startswith("#"):
                self.drop_anchor = True  # inline comment marker like [a]
                return
            self.href = unwrap_google_redirect(href)
            self.link_text = ""
        elif tag == "img":
            src = a.get("src") or ""
            if self.cur is None:
                self.blocks.append(Block("p", [("img", src)]))
            else:
                self.cur.pieces.append(("img", src))
        elif tag == "br" and self.cur is not None:
            self.cur.pieces.append(("br",))

    def handle_endtag(self, tag):
        if self.done:
            return
        if tag in ("head", "style", "script", "title"):
            self.skip_depth = max(0, self.skip_depth - 1)
            return
        if tag == "a":
            if self.drop_anchor:
                self.drop_anchor = False
                return
            if self.href is not None:
                if self.cur is None:
                    self.cur = Block("p")
                self.cur.pieces.append(("a", self.link_text, self.href))
                self.href = None
        elif tag in BLOCK_TAGS:
            self._close_block()

    def handle_data(self, data):
        if self.done or self.skip_depth or self.drop_anchor:
            return
        if self.href is not None:
            self.link_text += data
        elif self.cur is not None:
            self.cur.pieces.append(("t", data))

    def _close_block(self):
        if self.cur is not None:
            self.blocks.append(self.cur)
            self.cur = None

    def close(self):
        super().close()
        self._close_block()


def clean_text(s: str) -> str:
    s = s.replace("\xa0", " ").replace("​", "").replace("﻿", "")
    return s


def md_link(text: str, href: str) -> str:
    text = clean_text(text)
    lead = text[: len(text) - len(text.lstrip())]
    trail = text[len(text.rstrip()):]
    label = text.strip()
    if not label:
        return text
    if "[" in label or "]" in label:
        warn(f"リンク文字列の [ ] を全角に置き換えました: {label}")
        label = label.replace("[", "［").replace("]", "］")
    dest = href.strip()
    dest = dest.replace(" ", "%20").replace("<", "%3C").replace(">", "%3E")
    if "(" in dest or ")" in dest:
        dest = f"<{dest}>"
    return f"{lead}[{label}]({dest}){trail}"


@dataclass
class Line:
    tag: str
    md: str  # markdown text (links as [text](url)), images removed
    plain: str  # text only (link labels kept, urls dropped)
    images: list[str]
    img_first: bool  # image appears before any text


def blocks_to_lines(blocks: list[Block]) -> list[Line]:
    lines: list[Line] = []
    for b in blocks:
        # split by <br>
        segments: list[list] = [[]]
        for p in b.pieces:
            if p[0] == "br":
                segments.append([])
            else:
                segments[-1].append(p)
        for seg in segments:
            # merge adjacent links with the same href (Docs splits styled runs)
            merged: list = []
            for p in seg:
                if p[0] == "a" and merged and merged[-1][0] == "a" and merged[-1][2] == p[2]:
                    merged[-1] = ("a", merged[-1][1] + p[1], p[2])
                else:
                    merged.append(p)
            md, plain, images = "", "", []
            img_first = False
            for p in merged:
                if p[0] == "t":
                    md += clean_text(p[1])
                    plain += clean_text(p[1])
                elif p[0] == "a":
                    md += md_link(p[1], p[2])
                    plain += clean_text(p[1])
                elif p[0] == "img":
                    if not images and not plain.strip():
                        img_first = True
                    images.append(p[1])
            md = re.sub(r"[ \t]+$", "", md.strip())
            if md or images:
                lines.append(Line(b.tag, md, plain.strip(), images, img_first))
    return lines


# --------------------------------------------------------------------------
# lines -> episode
# --------------------------------------------------------------------------

LABEL_SHOW = re.compile(r"^(show\s*notes?)\s*[:：]\s*(.*)$", re.I)
LABEL_EDITORIAL = re.compile(r"^(editorial\s*notes?|編集後記)\s*[:：]\s*(.*)$", re.I)
LABEL_PERFORMERS = re.compile(r"^(出演者|performers?|cast)\s*[:：]\s*(.*)$", re.I)
LABEL_TOPICS = re.compile(r"^(トピック|topics?)\s*[:：]\s*(.*)$", re.I)
LABEL_GUESTS = re.compile(r"^(ゲスト名|guests)\s*[:：]\s*(.*)$", re.I)
LABEL_SUMMARY = re.compile(r"^(summary|概要|要約)\s*[:：]\s*(.*)$", re.I)
LABEL_TITLE_IDEAS = re.compile(r"^タイトル案\s*[:：]?\s*$")
MD_LINK = re.compile(r"\[([^\]]*)\]\((<[^>]+>|[^)]*)\)")


def split_list(value: str) -> list[str]:
    value = re.sub(r"[\"“”„'‘’「」『』\[\]]", "", value)
    return [x.strip() for x in re.split(r"[,、，;；]", value) if x.strip()]


@dataclass
class Episode:
    number: str
    title: str
    summary_html: str
    performers: list[str]
    topics: list[str]
    guests: list[str]
    note_lines: list[str]
    figures: list[tuple[str, str]]  # (source image path in export, caption)
    editorial_lines: list[str]


def summary_to_html(md: str) -> str:
    def repl(m):
        href = m.group(2).strip("<>").replace("'", "%27")
        return f"<a href='{href}'>{m.group(1)}</a>"
    return MD_LINK.sub(repl, md)


def parse_episode(lines: list[Line]) -> Episode:
    number = title = None
    start = 0
    for i, ln in enumerate(lines):
        m = re.match(r"^#?\s*(\d{1,4})\s+(.+)$", ln.plain)
        if m:
            number, title = m.group(1), f"#{m.group(1)} {m.group(2).strip()}"
            start = i + 1
            break
    if number is None:
        sys.exit("ERROR: 「#116 タイトル」のような番号付きタイトル行が見つかりません")

    state = "head"
    skipping_ideas = False
    summary: list[str] = []
    performers: list[str] | None = None
    topics: list[str] | None = None
    guests: list[str] = []
    pre_notes: list[Line] = []
    notes: list[Line] = []
    editorial: list[Line] = []

    for ln in lines[start:]:
        t = ln.md.strip()
        if state == "head":
            if LABEL_TITLE_IDEAS.match(t):
                skipping_ideas = True
                continue
            if skipping_ideas:
                if ln.tag == "li" or not t:
                    continue
                skipping_ideas = False
            m = LABEL_SHOW.match(t)
            if m:
                state = "notes"
                if m.group(2):
                    notes.append(Line(ln.tag, m.group(2), m.group(2), ln.images, False))
                continue
            if (m := LABEL_PERFORMERS.match(t)):
                performers = split_list(m.group(2))
            elif (m := LABEL_TOPICS.match(t)):
                topics = split_list(m.group(2))
            elif (m := LABEL_GUESTS.match(t)):
                guests = split_list(m.group(2))
            elif (m := LABEL_SUMMARY.match(t)):
                if m.group(2):
                    summary.append(m.group(2))
            elif not t and not ln.images:
                continue
            elif performers is None and topics is None and "お便り募集" not in t:
                summary.append(t)
            else:
                pre_notes.append(ln)
        elif state == "notes":
            m = LABEL_EDITORIAL.match(t)
            if m:
                state = "editorial"
                if m.group(2):
                    editorial.append(Line(ln.tag, m.group(2), m.group(2), [], False))
                continue
            notes.append(ln)
        else:
            editorial.append(ln)

    if state == "head":
        sys.exit("ERROR: 「Show Notes:」の見出しが見つかりません")
    if state != "editorial":
        warn("「Editorial Notes:」の見出しが見つかりません (空のまま作ります)")
    if not summary:
        warn("要約 (summary) が見つかりません")
    if performers is None:
        warn("「出演者:」の行が見つかりません")
    if topics is None:
        warn("「トピック:」の行が見つかりません")

    note_lines, figures = build_notes(pre_notes + notes)
    editorial_lines = []
    for ln in editorial:
        if ln.images:
            warn("Editorial Notes 内の画像は Show Notes の最後に移しました")
            figures += [(src, "") for src in ln.images]
        if ln.md:
            editorial_lines.append(ln.md)

    return Episode(
        number=number,
        title=title,
        summary_html=summary_to_html(" ".join(summary)),
        performers=performers or [],
        topics=topics or [],
        guests=guests,
        note_lines=note_lines,
        figures=figures,
        editorial_lines=editorial_lines,
    )


def build_notes(lines: list[Line]) -> tuple[list[str], list[tuple[str, str]]]:
    """Show Notes の行と画像を分ける。画像は最後に <figure> でまとめる (README のルール)。

    キャプションの推定:
      - 画像だけの行 → 直前の短いテキスト行 (リンクなし) をキャプションにして、その行は消す
      - 画像の直後が (カッコ書き) だけ → それをキャプションにして、その行は消す
      - テキスト付きの行に画像 → 行は残し、テキストをキャプションにする
    """
    items: list[str] = []
    figures: list[tuple[str, str]] = []
    caption_candidate = False  # items[-1] can become a caption
    for ln in lines:
        md = ln.md.strip()
        if not ln.images:
            if md:
                items.append(md)
                caption_candidate = (not MD_LINK.search(md) and len(ln.plain) <= 80
                                     and not md.startswith(("※", "*")))
            continue
        if not md:
            caption = ""
            if caption_candidate and items:
                caption = re.sub(r"[:：]\s*$", "", items.pop()).strip()
            figures += [(src, caption) for src in ln.images]
        else:
            paren = re.fullmatch(r"[（(](.+)[）)]", md)
            if ln.img_first and not MD_LINK.search(md):
                caption = paren.group(1) if paren else md
                figures += [(src, caption) for src in ln.images]
            else:
                items.append(md)
                figures += [(src, ln.plain) for src in ln.images]
        caption_candidate = False
    return items, figures


# --------------------------------------------------------------------------
# helpers
# --------------------------------------------------------------------------

def make_slug(title: str) -> str:
    t = re.sub(r"^#\d+\s*", "", title)
    t = re.sub(r"[(（][^)）]*[)）]", lambda m: m.group(0) if m.group(0).isascii() else " ", t)
    t = t.replace("’", "").replace("'", "")
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode()
    t = re.sub(r"[^A-Za-z0-9]+", "-", t).strip("-")
    return re.sub(r"-{2,}", "-", t)


def yaml_str(s: str) -> str:
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def yaml_list(items: list[str]) -> str:
    return "[" + ", ".join(json.dumps(x, ensure_ascii=False) for x in items) + "]"


def fetch(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read()


def title_matches(title: str, number: str) -> bool:
    return re.match(rf"^#?{number}(?!\d)", title.strip()) is not None


def fetch_apple(number: str) -> str:
    data = json.loads(fetch(f"https://itunes.apple.com/lookup?id={APPLE_PODCAST_ID}"
                            f"&entity=podcastEpisode&limit=200&country=jp"))
    for r in data.get("results", []):
        if r.get("wrapperType") == "podcastEpisode" and title_matches(r.get("trackName", ""), number):
            path = urlparse(r["trackViewUrl"]).path  # /us/podcast/<slug>/id1556937028
            path = re.sub(r"^/[a-z]{2}/", "/jp/", path)
            return f"https://embed.podcasts.apple.com{path}?i={r['trackId']}"
    return ""


def fetch_spotify(number: str) -> str:
    root = ET.fromstring(fetch(RSS_URL))
    link = ""
    for item in root.iter("item"):
        if title_matches(item.findtext("title") or "", number):
            link = item.findtext("link") or ""
            break
    if not link:
        return ""
    page = fetch(link).decode("utf-8", "replace").replace("\\u002F", "/")
    candidates: list[str] = []
    for m in re.finditer(rf'"title":"#?{number}(?!\d)', page):
        for sid in re.findall(r'"spotifyUrl":"https://open\.spotify\.com/episode/([A-Za-z0-9]{22})"',
                              page[m.end(): m.end() + 4000])[:1]:
            if sid not in candidates:
                candidates.append(sid)
    for sid in candidates:  # 念のため Spotify 側のタイトルで確認する
        info = json.loads(fetch("https://open.spotify.com/oembed?url="
                                + quote(f"https://open.spotify.com/episode/{sid}", safe="")))
        if title_matches(info.get("title", ""), number):
            return f"https://open.spotify.com/embed/episode/{sid}?utm_source=generator"
    return ""


def fetch_links(number: str) -> tuple[str, str]:
    spotify = apple = ""
    try:
        spotify = fetch_spotify(number)
    except Exception as e:  # network errors etc.
        warn(f"Spotify の URL 取得に失敗しました: {e}")
    try:
        apple = fetch_apple(number)
    except Exception as e:
        warn(f"Apple Podcasts の URL 取得に失敗しました: {e}")
    if not spotify:
        warn(f"Spotify に #{number} がまだ見つかりません。配信後に --fill-links {number} を実行してください")
    if not apple:
        warn(f"Apple Podcasts に #{number} がまだ見つかりません。配信後に --fill-links {number} を実行してください")
    return spotify, apple


def find_post(root: Path, number: str) -> Path | None:
    for p in sorted((root / "_posts").glob("*.md")):
        fm, _, _ = check_posts.parse_front_matter(p.read_text(encoding="utf-8"))
        if fm and str(fm.get("episode_number", "")).strip() == number:
            return p
    return None


def past_guest_episodes(root: Path, guests: list[str], exclude: Path | None = None) -> list[str]:
    hits = []
    for p in sorted((root / "_posts").glob("*.md")):
        if exclude is not None and p.resolve() == exclude.resolve():
            continue
        fm, _, _ = check_posts.parse_front_matter(p.read_text(encoding="utf-8"))
        if fm and isinstance(fm.get("guests"), list) and set(fm["guests"]) & set(guests):
            hits.append(f"#{fm.get('episode_number')}")
    return hits


def find_html(src: Path, tmp: Path) -> Path:
    if src.is_file() and src.suffix.lower() == ".zip":
        with zipfile.ZipFile(src) as z:
            z.extractall(tmp)  # zipfile strips absolute paths and ".."
        src = tmp
    if src.is_file() and src.suffix.lower() in (".html", ".htm"):
        return src
    if src.is_dir():
        found = sorted(src.rglob("*.html"))
        if len(found) == 1:
            return found[0]
        if not found:
            sys.exit(f"ERROR: {src} に .html ファイルがありません")
        sys.exit("ERROR: .html が複数あります。どれか1つを直接指定してください:\n  "
                 + "\n  ".join(str(f) for f in found))
    sys.exit(f"ERROR: {src} が見つからないか、zip / フォルダ / .html ではありません")


# --------------------------------------------------------------------------
# commands
# --------------------------------------------------------------------------

def render_post(ep: Episode, date: str, slug: str, spotify: str, apple: str,
                image_names: dict[str, str]) -> str:
    y, m, d = date.split("-")
    fm = [
        "---",
        "layout: episode",
        f"title: {yaml_str(ep.title)}",
        f'episode_number: "{ep.number}"',
        f"date: {date}",
        f"permalink: /{y}/{m}/{d}/{ep.number}-{slug}/",
        f"spotify: {yaml_str(spotify)}",
        f"apple_podcast: {yaml_str(apple)}",
    ]
    if ep.guests:
        fm.append(f"guests: {yaml_list(ep.guests)}")
    fm += [
        f"performers: {yaml_list(ep.performers)}",
        f"topics: {yaml_list(ep.topics)}",
        f"summary: {yaml_str(ep.summary_html)}",
        "---",
        "",
    ]
    body = ["Show Notes:"] + ep.note_lines
    if ep.figures:
        body.append("")
        for src, caption in ep.figures:
            body += ["<figure>",
                     f'  <img src="/assets/episodes/{ep.number}-{slug}/{image_names[src]}" alt="">']
            if caption:
                body.append(f"  <figcaption>{html.escape(caption, quote=False)}</figcaption>")
            body.append("</figure>")
        body.append("")
    body += ["", "Editorial Notes:"] + ep.editorial_lines
    return "\n".join(fm + body) + "\n"


def cmd_new(args) -> int:
    root = Path(args.root).resolve()
    src = Path(args.source).expanduser()
    with tempfile.TemporaryDirectory() as tmp:
        html_path = find_html(src, Path(tmp))
        parser = DocParser()
        parser.feed(html_path.read_text(encoding="utf-8"))
        parser.close()
        ep = parse_episode(blocks_to_lines(parser.blocks))

        if args.guests:
            ep.guests = split_list(args.guests)
        if "ゲスト" in ep.performers and not ep.guests:
            warn("ゲスト回ですが guests が空です。--guests \"名前,名前\" で指定してください (関連エピソード表示に使われます)")
        if ep.guests:
            past = past_guest_episodes(root, ep.guests)
            if past and "再登場" not in ep.topics:
                pos = ep.topics.index("ゲスト回") + 1 if "ゲスト回" in ep.topics else 0
                ep.topics.insert(pos, "再登場")
                print(f"・ゲストの過去出演回 ({', '.join(past)}) があるので topics に「再登場」を追加しました")
        unknown = [p for p in ep.performers if p not in check_posts.HOSTS]
        if unknown:
            warn(f"出演者は 萩/脇/藤/ゲスト のみ使います: {unknown}")

        date = args.date or dt.datetime.now(dt.timezone(dt.timedelta(hours=9))).strftime("%Y-%m-%d")
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", date):
            sys.exit("ERROR: --date は YYYY-MM-DD で指定してください")
        slug = args.slug or make_slug(ep.title)
        if not slug:
            sys.exit("ERROR: タイトルから英数字の slug を作れません。--slug で指定してください")

        spotify = apple = ""
        if not args.no_fetch:
            spotify, apple = fetch_links(ep.number)

        image_names: dict[str, str] = {}
        for src_rel, _ in ep.figures:
            if src_rel not in image_names:
                ext = Path(src_rel).suffix.lower() or ".jpg"
                image_names[src_rel] = f"image{len(image_names) + 1}{ext}"

        post_path = root / "_posts" / f"{date}-{ep.number}-{slug}.md"
        asset_dir = root / "assets" / "episodes" / f"{ep.number}-{slug}"
        content = render_post(ep, date, slug, spotify, apple, image_names)

        if args.dry_run:
            print(content)
            for s, n in image_names.items():
                print(f"[dry-run] {s} -> {asset_dir.relative_to(root)}/{n}")
            print_warnings()
            return 0

        existing = find_post(root, ep.number)
        if existing and existing.resolve() != post_path.resolve():
            sys.exit(f"ERROR: #{ep.number} は既に {existing.relative_to(root)} にあります")
        if (post_path.exists() or asset_dir.exists()) and not args.force:
            sys.exit(f"ERROR: {post_path.relative_to(root)} または画像フォルダが既にあります (上書きするなら --force)")

        post_path.parent.mkdir(parents=True, exist_ok=True)
        post_path.write_text(content, encoding="utf-8")
        if image_names:
            asset_dir.mkdir(parents=True, exist_ok=True)
            for s, n in image_names.items():
                img_src = (html_path.parent / s).resolve()
                if not img_src.is_file():
                    warn(f"画像が見つかりません: {s}")
                    continue
                shutil.copyfile(img_src, asset_dir / n)

    print(f"\n作成: {post_path.relative_to(root)}")
    if image_names:
        print(f"画像: {asset_dir.relative_to(root)}/")
        for (s, caption) in ep.figures:
            print(f"  {image_names[s]:<12} ← {s}   キャプション: {caption or '(なし)'}")
    return finish(post_path, root)


def cmd_fill_links(args) -> int:
    root = Path(args.root).resolve()
    number = args.fill_links.lstrip("#")
    post = find_post(root, number)
    if post is None:
        sys.exit(f"ERROR: episode_number が {number} の投稿が _posts にありません")
    text = post.read_text(encoding="utf-8")
    fm, _, _ = check_posts.parse_front_matter(text)
    spotify, apple = fetch_links(number)
    changed = []
    for key, value in (("spotify", spotify), ("apple_podcast", apple)):
        if not value:
            continue
        current = str(fm.get(key, "")).strip()
        if current and not args.force:
            if current != value:
                print(f"・{key} は既に入っているので変更しません (上書きするなら --force)")
            continue
        line = f"{key}: {yaml_str(value)}"
        if re.search(rf"^{key}:.*$", text, flags=re.M):
            text = re.sub(rf"^{key}:.*$", lambda _m: line, text, count=1, flags=re.M)
        else:
            text = re.sub(r"^(spotify:.*)$", lambda m_: m_.group(1) + "\n" + line, text, count=1, flags=re.M)
        changed.append(key)
    if changed:
        post.write_text(text, encoding="utf-8")
        print(f"更新: {post.relative_to(root)} ({', '.join(changed)})")
    return finish(post, root)


def print_warnings() -> None:
    if warnings:
        print("\n要確認:")
        for w in warnings:
            print(f"  ・{w}")


def finish(post: Path, root: Path) -> int:
    print_warnings()
    issues = check_posts.check_file(post, root, check_posts.all_post_paths(root))
    print("\nチェック結果:")
    for i in issues:
        print(f"  {i.level}: {i.line}行目: {i.message}")
    if not issues:
        print("  問題なし")
    print("\n次は内容を確認して、git add → commit → push してください。")
    return 1 if any(i.level == "ERROR" for i in issues) else 0


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Google Docs の原稿 (ウェブページ形式の書き出し) から新エピソードを作ります。",
        epilog="例: python3 tools/new_episode.py ~/Downloads/116Dr._HammerfromU.zip --guests \"長濱健一郎\"")
    ap.add_argument("source", nargs="?", help="Google Docs から書き出した zip / フォルダ / .html")
    ap.add_argument("--date", help="公開日 YYYY-MM-DD (省略時は今日)")
    ap.add_argument("--slug", help="URL 用の英数字名 (省略時はタイトルから自動生成)")
    ap.add_argument("--guests", help="ゲストの実名をカンマ区切りで")
    ap.add_argument("--no-fetch", action="store_true", help="Spotify / Apple の URL を取りに行かない")
    ap.add_argument("--dry-run", action="store_true", help="ファイルを書かずに結果を表示")
    ap.add_argument("--force", action="store_true", help="既存のファイル / URL を上書き")
    ap.add_argument("--fill-links", metavar="番号", help="既存の投稿に Spotify / Apple の URL を埋める")
    ap.add_argument("--root", default=str(ROOT), help=argparse.SUPPRESS)
    args = ap.parse_args()
    if args.fill_links:
        return cmd_fill_links(args)
    if not args.source:
        ap.print_help()
        return 2
    return cmd_new(args)


if __name__ == "__main__":
    sys.exit(main())

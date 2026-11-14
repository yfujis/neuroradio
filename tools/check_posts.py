#!/usr/bin/env python3
"""NeuroRadio のエピソード (_posts/*.md) をチェックする。

使い方:
  python3 tools/check_posts.py              # 全エピソード
  python3 tools/check_posts.py _posts/2026-11-14-116-Dr-Hammer-from-U.md

ERROR が1つでもあれば終了コード 1 を返します。WARN は確認推奨です。
"""
from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parent.parent
HOSTS = {"萩", "脇", "藤", "ゲスト"}
# これ以降の回はファイル名と permalink を揃える (それ以前は旧サイトのURLを維持しているので対象外)
FIRST_NEW_STYLE_EPISODE = 105
REQUIRED_KEYS = ["layout", "title", "episode_number", "date", "permalink",
                 "spotify", "performers", "topics", "summary"]
SHOW_NOTES_LABELS = {"show notes", "shownotes", "show note"}
EDITORIAL_LABELS = {"editorial notes", "editorial note", "編集後記"}

# _plugins/episode_parser.rb と同じ解釈: <...> で囲まなければ最初の ")" でURLが終わる
LINK_RE = re.compile(r"(!?)\[([^\]]*)\]\((<[^>]+>|[^)]*)\)")
NEW_STYLE_NAME = re.compile(r"^(\d{4})-(\d{2})-(\d{2})-(\d+)-(.+)\.md$")
ANY_NAME = re.compile(r"^(\d{4})-(\d{2})-(\d{2})-(.+)\.md$")


@dataclass
class Issue:
    level: str  # "ERROR" or "WARN"
    path: Path
    line: int
    message: str

    def __str__(self) -> str:
        try:
            shown = self.path.relative_to(Path.cwd())
        except ValueError:
            shown = self.path
        return f"{shown}:{self.line}: {self.level}: {self.message}"


def parse_front_matter(text: str):
    """Return (data, body, body_start_line). Handles the simple YAML used in _posts."""
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        return None, text, 1
    data: dict[str, object] = {}
    line_of: dict[str, int] = {}
    key = None
    for i in range(1, len(lines)):
        raw = lines[i]
        if raw.strip() == "---":
            body = "\n".join(lines[i + 1:])
            for k, v in list(data.items()):
                data[k] = _yaml_value(str(v))
            data["__lines__"] = line_of
            return data, body, i + 2
        m = re.match(r"^([A-Za-z_][\w-]*):\s?(.*)$", raw)
        if m:
            key = m.group(1)
            data[key] = m.group(2)
            line_of[key] = i + 1
        elif key is not None:
            data[key] = str(data[key]) + "\n" + raw
    return None, text, 1


def _yaml_value(value: str):
    v = value.strip()
    if v.startswith("[") and v.endswith("]"):
        try:
            return json.loads(v)
        except json.JSONDecodeError:
            return [x.strip().strip("\"'") for x in v[1:-1].split(",") if x.strip()]
    if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
        return v[1:-1]
    return v


def check_file(path: Path, root: Path = ROOT, all_posts: list[Path] | None = None) -> list[Issue]:
    issues: list[Issue] = []

    def add(level: str, line: int, msg: str) -> None:
        issues.append(Issue(level, path, line, msg))

    text = path.read_text(encoding="utf-8")
    fm, body, body_start = parse_front_matter(text)
    if fm is None:
        add("ERROR", 1, "front matter (--- で囲まれた冒頭部分) が見つかりません")
        return issues
    ln = fm.get("__lines__", {})

    # ---- front matter ----
    for k in REQUIRED_KEYS:
        if k not in fm:
            add("ERROR", 1, f"front matter に {k}: がありません")

    num = str(fm.get("episode_number", "")).strip()
    title = str(fm.get("title", ""))
    m = re.match(r"^#(\d+)\b", title)
    if num and m and m.group(1) != num:
        add("ERROR", ln.get("title", 1), f"title の番号 #{m.group(1)} と episode_number {num} が違います")

    spotify = str(fm.get("spotify", "")).strip()
    if "spotify" in fm:
        if not spotify:
            add("ERROR", ln.get("spotify", 1), "spotify が空です (tools/new_episode.py --fill-links で取得できます)")
        elif not spotify.startswith("https://open.spotify.com/embed/episode/"):
            add("ERROR", ln.get("spotify", 1), "spotify は https://open.spotify.com/embed/episode/... の埋め込みURLにしてください")

    if not str(fm.get("apple_podcast", "")).strip():
        add("WARN", ln.get("apple_podcast", 1), "apple_podcast が空です (tools/new_episode.py --fill-links で取得できます)")

    performers = fm.get("performers") or []
    if isinstance(performers, list):
        unknown = [p for p in performers if p not in HOSTS]
        if unknown:
            add("WARN", ln.get("performers", 1), f"performers は 萩/脇/藤/ゲスト のみ使います: {unknown}")
        if "ゲスト" in performers and not fm.get("guests"):
            add("WARN", ln.get("performers", 1), "ゲスト回ですが guests: (ゲストの実名) がありません")

    date = str(fm.get("date", "")).strip()[:10]
    permalink = str(fm.get("permalink", "")).strip()
    name_m = ANY_NAME.match(path.name)
    if name_m and date:
        fdate = "-".join(name_m.groups()[:3])
        if date != fdate:
            add("ERROR", ln.get("date", 1), f"date ({date}) とファイル名の日付 ({fdate}) が違います")
        if permalink and not permalink.startswith("/" + fdate.replace("-", "/") + "/"):
            add("ERROR", ln.get("permalink", 1), f"permalink がファイル名の日付 ({fdate}) で始まっていません")
    new_m = NEW_STYLE_NAME.match(path.name)
    if new_m and permalink and num.isdigit() and int(num) >= FIRST_NEW_STYLE_EPISODE:
        y, mo, d, fnum, slug = new_m.groups()
        expected = f"/{y}/{mo}/{d}/{fnum}-{slug}/"
        if permalink != expected:
            add("ERROR", ln.get("permalink", 1), f"permalink はファイル名に合わせて {expected} にしてください")
        if num and fnum != num:
            add("ERROR", ln.get("episode_number", 1), f"ファイル名の番号 {fnum} と episode_number {num} が違います")

    if num and all_posts:
        for other in all_posts:
            if other.resolve() == path.resolve():
                continue
            ofm, _, _ = parse_front_matter(other.read_text(encoding="utf-8"))
            if ofm and str(ofm.get("episode_number", "")).strip() == num:
                add("ERROR", ln.get("episode_number", 1), f"episode_number {num} が {other.name} と重複しています")

    # ---- body ----
    labels = set()
    for offset, raw in enumerate(body.split("\n")):
        lineno = body_start + offset
        line = raw.strip()
        label = re.sub(r"[:：]\s*$", "", line).strip().lower()
        if label in SHOW_NOTES_LABELS:
            labels.add("show")
        if label in EDITORIAL_LABELS:
            labels.add("editorial")

        for lm in LINK_RE.finditer(line):
            dest = lm.group(3)
            if dest.startswith("<"):
                if "\\(" in dest or "\\)" in dest:
                    add("ERROR", lineno, f"URL の \\( \\) はバックスラッシュ不要です: {dest}")
            elif "\\" in dest:
                add("ERROR", lineno, f"URL に \\ があるとリンクが壊れます。括弧入りURLは <...> で囲んでください: {dest}")
            elif "(" in dest:
                add("ERROR", lineno, f"URL に括弧があるので <...> で囲んでください (このままだと途中で切れます): {dest}")
            elif not dest.strip():
                add("ERROR", lineno, "リンク先 URL が空です")
            elif " " in dest.strip():
                add("WARN", lineno, f"URL に空白が入っています: {dest}")
            target = unquote(dest.strip("<>").strip())
            if target.startswith("/assets/") and not (root / target.lstrip("/")).exists():
                add("ERROR", lineno, f"画像/ファイルが見つかりません: {target}")

        for src in re.findall(r"""src=["'](/assets/[^"']+)["']""", line):
            if not (root / unquote(src).lstrip("/")).exists():
                add("ERROR", lineno, f"画像が見つかりません: {src}")

        if re.search(r"\[\[[a-z]+\]\]\(#cmnt", line):
            add("ERROR", lineno, "Google Docs のコメント ([a] など) が残っています")
        stripped_links = LINK_RE.sub(lambda m_: m_.group(2), line)
        if re.search(r"\\[_*\[\]`]", stripped_links):  # \# は意図的な表記として許可
            add("WARN", lineno, "\\_ のようなエスケープはそのまま文字として表示されます")
        if "TODO" in line:
            add("WARN", lineno, "TODO が残っています")

    if "show" not in labels:
        add("ERROR", body_start, "Show Notes: の見出しがありません")
    if "editorial" not in labels:
        add("ERROR", body_start, "Editorial Notes: の見出しがありません")
    return issues


def all_post_paths(root: Path = ROOT) -> list[Path]:
    return sorted((root / "_posts").glob("*.md"))


def main(argv: list[str]) -> int:
    root = ROOT
    posts = all_post_paths(root)
    targets = [Path(a).resolve() for a in argv] if argv else posts
    issues: list[Issue] = []
    for p in targets:
        issues += check_file(p, root, posts)
    for issue in issues:
        print(issue)
    errors = sum(i.level == "ERROR" for i in issues)
    warns = sum(i.level == "WARN" for i in issues)
    print(f"\n{len(targets)} ファイルをチェック: ERROR {errors} 件, WARN {warns} 件")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

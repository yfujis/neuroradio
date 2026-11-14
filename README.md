# NeuroRadio Jekyll Site

NeuroRadioのGitHub Pages向けJekyllサイトです。エピソードは `_posts/` のMarkdownファイルとして管理します。

## ツールで新しいエピソードを作る（おすすめ）

Google Docsの原稿から、投稿ファイルと画像フォルダを自動で作れます。Python 3だけで動きます（追加インストール不要）。

1. Google Docsで「ファイル → ダウンロード → ウェブページ（.html、zip）」を選ぶ
2. リポジトリのフォルダで、ダウンロードしたzip（または展開したフォルダ）を指定して実行する

```bash
python3 tools/new_episode.py ~/Downloads/116Dr._HammerfromU.zip --guests "長濱健一郎,小坂田拓哉"
```

自動でやること:

- タイトル行の `#番号` から、ファイル名・`permalink`・画像フォルダ名を決める（日付は今日。変えるときは `--date 2026-12-01`。slugは英語タイトルから作り、英語がなければ `--slug` で指定）
- 要約（収録日を含む）・出演者・トピックをfront matterに入れる
- Show Notes / Editorial Notesを1行1項目に整形する。Docsのコメントやタイトル案は除く
- 括弧を含むURLは `<>` で囲む
- 画像を `image1.jpg` からの連番でコピーし、Show Notesの最後に `<figure>` で並べる（キャプションは画像の直前の行などから推定するので、表示を確認してください）
- Spotify・Apple Podcastsの埋め込みURLを取得する。配信前で見つからなければ空欄にするので、配信後に `python3 tools/new_episode.py --fill-links 116` で埋める
- 同じゲストの過去回があれば、topicsに `再登場` を足す

Docs側は、冒頭の `#116 タイトル` 行、要約の段落、`出演者:` 行、`トピック:` 行、`Show Notes:` と `Editorial Notes:` の見出しがあれば読めます。`ゲスト名: 長濱健一郎, 小坂田拓哉` の行を入れておくと `--guests` は不要です。書き込まずに結果だけ見たいときは `--dry-run` を付けます。

### 投稿のチェック

```bash
python3 tools/check_posts.py                                        # 全エピソード
python3 tools/check_posts.py _posts/2026-11-14-116-Dr-Hammer-from-U.md
```

壊れるリンク（`\(` や、`<>` で囲んでいない括弧入りURL）、ファイル名・日付・permalinkの食い違い、存在しない画像、空のSpotify URL、Docsのコメントの残りなどを見つけます。pushの前に実行してください。

## 新しいエピソードを手で追加する

新しいエピソードは `_posts/` にMarkdownファイルを1つ追加すると作れます。

ファイル名は `YYYY-MM-DD-slug.md` にします。

```text
_posts/2026-06-01-new-episode-title.md
```

`slug` はURLに入る英数字の短い名前です。元サイトとURLを揃えるため、`permalink` にはエピソード番号を含めます。

```text
/2026/06/01/105-new-episode-title/
```

### テンプレート

以下をコピーして、新しいファイルに貼り付けてください。

```markdown
---
layout: episode
title: "#105 New Episode Title"
episode_number: "105"
date: 2026-06-01
permalink: /2026/06/01/105-new-episode-title/
spotify: "https://open.spotify.com/embed/episode/..."
performers: ["ゲスト", "脇", "藤"]
topics: ["ゲスト回", "論文解説"]
summary: "ここにエピソードの短い説明を書きます。"
---

Show Notes:
1つ目のShow Note
2つ目のShow Note

Editorial Notes:
編集後記をここに書きます。（藤島）
複数人のコメントは項目を分けると読みやすいです。（宮脇）
```

### 書き方

`Show Notes:` と `Editorial Notes:` のラベルは消さないでください。Jekyll pluginがこのラベルを読んで、現在のデザインに変換します。

要約は本文の `Summary:` ではなく、front matter の `summary:` にだけ書きます。

Show NotesとEditorial Notesは、Google Docsからそのまま貼りやすいように、各項目の先頭に `-` を付けなくて大丈夫です。1行が1項目として表示されます。

リンクはMarkdown形式で書きます。

```markdown
[表示テキスト](https://example.com)
```

URL に `(` や `)` が入る場合は、リンク先を `<>` で囲ってください。Wikipedia や Cell Press の URL で起こりやすいです。

```markdown
[Sting](<https://en.wikipedia.org/wiki/Sting_(musician)>)
```

### Spotify埋め込みURL

Spotifyのエピソードページから埋め込みURLを取得し、`spotify:` に入れます。形式はこのようにします。

```text
https://open.spotify.com/embed/episode/xxxxxxxxxxxxxxxxxxxxxx?utm_source=generator
```

### 出演者とトピック

`performers` と `topics` はエピソード一覧のフィルターに使われます。出演者タグではゲストの個人名は使わず、ゲストがいる回は `ゲスト` と書きます。

ホストは短い表記にします。

```text
萩, 脇, 藤
```

同じゲストが再登場する回やシリーズ回では、`topics` に `再登場` を入れます。

例:

```yaml
performers: ["ゲスト", "萩", "脇"]
topics: ["ゲスト回", "論文解説", "留学", "再登場"]
```

### 画像を入れる場合

画像ファイルはエピソードごとのフォルダに入れます。

```text
assets/episodes/105-new-episode-title/image1.jpg
```

画像はShow Notesの最後、`Editorial Notes:` の直前に置きます。キャプションがある場合は `<figcaption>` に書きます。

```html
<figure>
  <img src="/assets/episodes/105-new-episode-title/image1.jpg" alt="">
  <figcaption>ここにキャプションを書きます。</figcaption>
</figure>
```

キャプションがない場合:

```html
<figure>
  <img src="/assets/episodes/105-new-episode-title/image1.jpg" alt="">
</figure>
```
画像はキャプションがなければ、マークダウンの画像形式で書いても大丈夫です。

```markdown
![代替テキスト](/assets/episodes/105-new-episode-title/image1.jpg)
```

変更したら、GitHubにpushしてください。GitHub Actionsが自動でサイトをビルドしてデプロイします。Actionsで、デプロイが成功したかどうかを確認できます。

## 既存エピソードを編集する

既存エピソードは `_posts/` の該当ファイルを編集します。例:

```text
_posts/2026-04-08-real-projections-and-tangential-matters.md
```


## GitHub Pagesデプロイ

一度設定してあるので、いじる必要ないです。

GitHub PagesはGitHub Actionsで `_site/` をデプロイします。`.github/workflows/jekyll.yml` が `bundle exec jekyll build` を実行します。

現在の `_config.yml` は本番ドメイン `https://neuroradio.tokyo/` 用に `url: "https://neuroradio.tokyo"`、`baseurl: ""` にしています。

推奨設定:

1. GitHubで `Settings` -> `Pages` を開く。
2. Sourceを `GitHub Actions` にする。
3. mainブランチにpushする、またはworkflowを手動実行する。

## Notes

- `_posts/*.md` がエピソードの編集元です。
- `permalink` を元サイトと同じURLにすることで、移行後もURLを維持します。
- `_plugins/episode_parser.rb` が `Summary:`, `Show Notes:`, `Editorial Notes:` のラベル形式を読み取り、現在のデザインに合うHTMLへ変換します。
- 画像は `/assets/episodes/...` と書きます。本番では `https://neuroradio.tokyo/assets/episodes/...` として表示されます。
- `styles.css` と `script.js` は現在のNeuroRadioデザインをそのまま使います。

## Files

- `_posts/*.md` - エピソード本文
- `_layouts/episode.html` - 個別エピソードの見た目
- `_layouts/default.html` - 共通HTML
- `_includes/` - header/footer/tag UI
- `_plugins/episode_parser.rb` - ラベル形式のMarkdownを読むJekyll plugin
- `tools/new_episode.py` - Google Docsの書き出しから新エピソードを作るツール（サイトには含まれない）
- `tools/check_posts.py` - `_posts/` のチェックツール
- `index.html` - ホーム
- `episodes/index.html` - エピソード一覧
- `otayori/index.html` - お便りページ
- `styles.css` - responsive visual system
- `script.js` - mobile navigation and archive filtering/pagination

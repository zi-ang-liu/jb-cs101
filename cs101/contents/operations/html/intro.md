# HTMLによるウェブページ作成

**HTML**（HyperText Markup Language）は，ハイパーテキストを記述するためのマークアップ言語です．ウェブページを表示するために用いられます．HTMLで記述されたファイルは，`*.html`という拡張子を持ちます．

:::{note}
さて，ハイパーテキストとマークアップ言語とは何でしょうか？

**ハイパーテキスト**（HyperText）とは，ハイパーリンク（hyperlink）を通じて，他の文書やファイルへアクセスできるテキストのことです．例えば，「[こちら](https://www.google.com)」というリンクをクリックすると，Googleのウェブページに移動します．

**マークアップ言語**（Markup Language）とは，マークをつけて文書の構造や修飾などを記述する言語のことです．例えば，`<b>Example</b>`は，`Example`というテキストを太字で表示することを指示します．マークアップという言葉は，印刷物の作成時に，赤ペンやハイライトで文書にマークをつけることに由来します．
:::

## VS CodeでのHTMLファイルの作成

Visual Studio Code（VS Code）はMicrosoftが開発している統合開発環境（Integrated Development Environment, IDE）です。C、Python、Javaなどのプログラミング言語をサポートしており、HTML、CSSなどのウェブ開発にも対応しています。

VS Codeを使ってHTMLファイルを作成するには、以下の手順に従います：

1. 作業フォルダー「my_website」を作成します。
2. VS Codeを起動します。
3. 「ファイル」メニューから「フォルダーを開く」を選択し、「my_website」フォルダーを開きます。
4. 「ファイル」メニューから「新しいファイル」を選択し、`index.html`という名前でファイルを保存します。
5. 作成した`index.html`ファイルにHTMLコードを入力します。
6. <kbd>Ctrl</kbd> + <kbd>S</kbd>を押して保存します。
7. ブラウザで`index.html`ファイルを開くと、作成したウェブページが表示されます。

## 練習

以下のHTMLコードを`index.html`ファイルに入力して、ブラウザで表示してみましょう。

```html
<!DOCTYPE html>
<html>

<head>
  <title>Page Title</title>
</head>

<body>
  <h1>This is a Heading</h1>
  <p>This is a paragraph.</p>
  <p>This is another paragraph with <b>bold</b> text.</p>
</body>

</html>
```
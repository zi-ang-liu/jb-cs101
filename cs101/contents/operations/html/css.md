# CSS

HTMLで作成されたウェブページのスタイルを定義するために、**CSS**（Cascading Style Sheets）が使用されます。CSSを用いて、フォントの種類やサイズ、背景色、レイアウトなど、HTML要素の見た目を制御することができます。

「Separation of content and presentation」という考え方があり、HTMLとCSSはその代表例です。HTMLはウェブページの内容を記述し、CSSはその見た目を定義します。

##

CSSは、以下の三つの方法でHTMLに適用できます。

- **Inline**: HTML要素の`style`属性を使用して、直接スタイルを指定します。
- **Internal**: HTML文書内の`<style>`タグを使用して、スタイルを定義します。
- **External**: 別のCSSファイルを作成し、HTML文書の`<link>`タグを使用して読み込みます。

Externalは、一般的に最も推奨される方法です。

## Inline CSS

HTML要素の`style`属性を使用して、直接スタイルを指定します。例えば、以下のように記述します。

```html
<h1 style="color: blue;">A blue heading</h1>
<p style="color: red;">A red paragraph</p>
```

## Internal CSS

HTML文書内の`<style>`タグを使用して、スタイルを定義します。以下のように記述します。

```html
<!DOCTYPE html>
<html>

<head>
  <title>Internal CSS Example</title>
  <style>
    h1 {
      color: blue;
    }

    p {
      color: red;
    }
  </style>
</head>

<body>
  <h1>A blue heading</h1>
  <p>A red paragraph</p>
</body>

</html>
```

## External CSS

別のCSSファイルを作成し、HTML文書の`<link>`タグを使用して読み込みます。

```
my_website/
├── index.html
└── assets/
    └── images/
├── css/
    └── styles.css
```

```html
<!DOCTYPE html>
<html>

<head>
  <title>Internal CSS Example</title>
  <link rel="stylesheet" href="css/styles.css">
</head>

<body>
  <h1>A blue heading</h1>
  <p>A red paragraph</p>
</body>

</html>
```

```css
h1 {
  color: blue;
}
p {
  color: red;
}
```
# 要素

HTMLは，**タグ**と呼ばれる特別な記号を使って，文書の構造や修飾などを記述します．タグには，**開始タグ**と**終了タグ**があります．開始タグと終了タグで囲まれた部分を**内容**と呼びます．開始タグ，内容，終了タグで構成される部分を**要素**と呼びます．

要素の一般的な書式は次の通りです：

```html
<要素名>内容</要素名>
```

タグは，`<`と`>`で囲まれた文字列です．終了タグは，**要素名**の前に`/`を付けて表現します．

## HTMLの基本型

下はHTMLの基本型を示す例です．

```html
<!DOCTYPE html>
<html>

<head>
  <meta charset="UTF-8">
  <title>Page Title</title>
</head>

<body>
  <h1>This is a heading</h1>
  <p>This is a paragraph.</p>
</body>

</html>
```

:::{note}
HTMLファイルの先頭には，`<!DOCTYPE html>`を記述します．これは，「HTML Living Standard」という最新のHTML仕様を使用することを示します．ここで注意すべき点は，`<!DOCTYPE html>`はタグではなく，文書型宣言（Document Type Declaration）であるということです．
:::

- html要素はHTML文書の最上位要素を表し、ルート要素と呼ばれます．html要素には、head要素とbody要素が含まれます。
  - head要素には、meta要素や文書のタイトルなどを記述します。
    - meta要素は、`<meta 属性名="属性値">`の形式で、文書のメタデータを指定します．`<meta charset="UTF-8">`は、文字コードをUTF-8に設定するためのタグです。
    - title要素は、文書のタイトルを指定します．
  - body要素には、文書の内容を記述します．
    - h1要素は、レベル1の見出しを表します．そのほかにも、h2, h3, ... h6までの見出し要素があります．
    - p要素は、段落を表します．

## HTMLの基本構造

HTMLは木構造を持つため，要素は入れ子構造になります．以下の例では，`<p>`タグの中に`<b>`タグが入れ子構造として含まれています．この時，p要素はb要素の親要素，b要素はp要素の子要素となります．

```html
<p>This is another paragraph with <b>bold</b> text.</p>
```

HTMLの基本型を木構造で表すと次のようになります．

```
html
├── head
│   └── title
└── body
    ├── h1
    └── p
```

## 練習

以上で紹介したHTMLの基本型を参考にして、自己紹介のWebページを作成してみましょう．

参考例

```html
<!DOCTYPE html>
<html>

<head>
  <meta charset="UTF-8">
  <title>Hosei Hanako's Web Page</title>
</head>

<body>
  <h1>Welcome to My Web Page</h1>
  <h2>About Me</h2>
  <p>Hello! My name is Hosei Hanako. I am a student at Hosei University.</p>
  <p>I love programming and web development.</p>
  <h2>My Hobbies</h2>
  <p>In my free time, I enjoy reading books, playing video games, and exploring new technologies.</p>
</body>

</html>
```
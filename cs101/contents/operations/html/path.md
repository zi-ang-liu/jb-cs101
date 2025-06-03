# パス

HTMLでは、外部からのファイルを読み込むために、パスを指定する必要があります。ここでは、`<img>`タグを使ってパスを指定する方法について説明します。

`<img>`要素は、画像を表示するために使用されます。書式は以下の通りです。

```html
<img src="画像のパス" alt="代替テキスト" width="幅" height="高さ">
```

- `src`属性は、画像のパスを指定するために使用されます。GIF、JPEG、SVGなどの画像ファイルを参照できます。
- `alt`属性は、画像が表示できない場合に代替テキストを提供するために使用されます。
- `width`と`height`属性は、画像の表示サイズを指定するために使用されます。

## URL

画像をウェブ上のURLから参照する場合、以下のように記述します。

```html
<img src="https://upload.wikimedia.org/wikipedia/commons/7/70/Example.png" alt="An example image">
```

```{note}
[Lorem Picsum](https://picsum.photos)は、ダミー画像を提供するサービスです。ダミー画像のサイズが指定できるため、ウェブサイトのデザインやレイアウトのテストに便利です。
```

## 相対パス

ローカルファイルを参照する場合、相対パスを使用します。例えば、以下のようなフォルダー構成を考えます。

```
my_website
├── index.html
└── picture.png
```

`picture.png`と`index.html`が同じフォルダーにある場合、`index.html`から`picture.png`を参照するには、以下のように記述します。

```html
<img src="picture.png" alt="a picture">
```

以下のフォルダー構成があるとします。

```
my_website
├── index.html
└── assets
    └── images
        └── picture.png
```

`index.html`から`picture.png`を参照するには、以下のように記述します。

```html
<img src="assets/images/picture.png" alt="a picture">
```

## ルート相対パス

以下のフォルダー構成があるとします。

```
my_website
├── index.html
└── assets
    └── images
        └── picture.png
```

ルートとは、「my_website」というフォルダーのことです。

ルート相対パスは`/`で始まるパスです。`/`はWebサイトのルートフォルダー（この場合は`my_website`）を指します。`picture.png`を参照するには、以下のように記述します。

```html
<img src="/assets/images/picture.png" alt="a picture">
```

## 練習

URL、相対パス、ルート相対パスを使用して、任意の画像を参照するHTMLファイルを作成してみましょう。

**参考例**

フォルダー構成は以下のようにします。

```
my_website
├── index.html
└── assets
    └── images
        └── book.png
        └── video_game.png
```

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
  <img src="assets/images/book.png" alt="an image of a book">
  <img src="/assets/images/video_game.png" alt="an image of a video game">
  <img src="https://upload.wikimedia.org/wikipedia/commons/7/79/Dampfturbine_Montage01.jpg" alt="an example of energy technology" width="300" height="200">

  <p>Author: Hosei Hanako</p>
</body>

</html>
```
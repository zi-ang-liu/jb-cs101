# 属性

要素には，**属性**を指定することができます．属性は，要素の振る舞いや外観を制御するための情報を提供します．属性は，開始タグに記述され，`属性名="属性値"`という形式で表現されます．

ここでは，`<a>`要素と`<img>`要素を例に、属性の使い方を説明します．

## a要素

`<a>`要素は、リンクを作成するために使用されます。aは「anchor」の略で、アンカー要素とも呼ばれます。書式は以下の通りです。

```html
<a href="リンク先のURL">リンクテキスト</a>
```

`herf`属性は、リンク先のURLを指定するために使用されます。

### ウェブサイトへのリンク

下記は、「Google」というテキストをクリックすると、Googleのウェブサイトに移動するリンクを作成する例です。

```html
<a href="https://www.google.com">Google</a>
```

### メールアドレスへのリンク

メールアドレスへのリンクを作成するには、`mailto:`を使用します。

以下の例では、「Send Email」というテキストをクリックすると、`someone@example.com`というメールアドレスにメールを送信するリンクを作成しています。

```html
<a href="mailto:someone@example.com">Send Email</a>
```

## img要素

`<img>`要素は、画像を表示するために使用されます。書式は以下の通りです。

```html
<img src="画像のURL" alt="代替テキスト">
```

- `src`属性は、画像のURLを指定するために使用されます。
- `alt`属性は、画像が表示できない場合に代替テキストを提供するために使用されます。

```html
<img src="https://upload.wikimedia.org/wikipedia/commons/7/70/Example.png" alt="An example image">      
```

「my_website」フォルダーは以下のような構成になっているとします。

```
my_website
├── index.html
└── images
    └── example.png
```

以下のように、`example.png`という画像ファイルを`images`フォルダーに保存している場合、HTMLファイルから画像を参照するには、相対パスを使用します。

```html
<img src="images/example.png" alt="An example image">
```

```{note}
[Lorem Picsum](https://picsum.photos)は、ダミー画像を提供するサービスです。ダミー画像のサイズが指定できるため、ウェブサイトのデザインやレイアウトのテストに便利です。
```

## 練習

以下の参考例を参考にして、自己紹介のウェブページを作成してみましょう。
- `<img>`要素を使用して好みの画像を表示する。
- `<a>`要素を使用して、メールアドレスへのリンクを作成する。
- `<a>`要素を使用して、Hosei Universityのウェブサイトへのリンクを作成する。

```html
<!DOCTYPE html>
<html>

<head>
  <meta charset="UTF-8">
  <title>Hosei Hanako's Web Page</title>
</head>

<body>
  <header>
    <h1>Welcome to My Web Page</h1>
  </header>

  <section>
    <h2>About Me</h2>
    <img src="https://picsum.photos/200" alt="A random image">
    <p>Hello! My name is Hosei Hanako. I am a student at <a href="https://www.hosei.ac.jp">Hosei University</a>.</p>
    <p>I love programming and web development.</p>
  </section>

  <section>
    <h2>My Hobbies</h2>
    <p>In my free time, I enjoy reading books, playing video games, and exploring new technologies.</p>
  </section>

  <footer>
    <p>Author: Hosei Hanako</p>
    <p>Email: <a href="mailto:hanako@example.com">hanako@example.com</a></p>
    <p>Affiliation:
      <a href="https://www.hosei.ac.jp/riko/">Faculty of Science and Engineering</a>,
      <a href="https://www.hosei.ac.jp">Hosei University</a><br>
    </p>
  </footer>
</body>

</html>
```
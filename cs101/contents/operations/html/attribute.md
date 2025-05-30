# 属性

要素には，**属性**を指定することができます．属性は，要素の振る舞いや外観を制御するための情報を提供します．属性は，開始タグに記述され，`属性名="属性値"`という形式で表現されます．

## a要素

a要素は、リンクを作成するために使用されます。aは「anchor」の略で、アンカー要素とも呼ばれます。書式は以下の通りです。

```html
<a href="リンク先のURL">リンクテキスト</a>
```

`herf`属性は、リンク先のURLを指定するために使用されます。

下記は、「Google」というテキストをクリックすると、Googleのウェブサイトに移動するリンクを作成する例です。

```html
<a href="https://www.google.com">Google</a>
```

## img要素

img要素は、画像を表示するために使用されます。書式は以下の通りです。

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


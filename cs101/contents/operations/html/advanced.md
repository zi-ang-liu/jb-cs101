# よく使うタグと属性

## 見出し

HTMLでは、見出しを作成するためにh1からh6までの要素を使用します。hは"heading"の略で、数字が小さいほど見出しのレベルが高くなります。

```html
<h1>Heading 1</h1>
<h2>Heading 2</h2>
<h3>Heading 3</h3>
<h4>Heading 4</h4>
<h5>Heading 5</h5>
<h6>Heading 6</h6>
```

## 改行

`<br>`要素は改行に使用します．

```html
<p>This is a line.<br>This is another line.</p>
```

:::{note}

段落分けのためには、p要素を使用します。

```html
<p>これは1つ目の段落です。</p>
<p>これは2つ目の段落です。</p>
```
:::

## img要素

`<img>`要素は、画像を表示するために使用されます。書式は以下の通りです。

```html
<img src="画像のURL" alt="代替テキスト">
```

- `src`属性は、画像のURLを指定するために使用されます。
- `alt`属性は、画像が表示できない場合に代替テキストを提供するために使用されます。
- `style`属性は，画像の幅や高さを指定するために使用できます。

### URLでの画像参照

画像をウェブ上のURLから参照する場合、以下のように記述します。

```html
<img src="https://upload.wikimedia.org/wikipedia/commons/7/70/Example.png" alt="An example image" style="width: 300px; height: auto;">
```

```{note}
[Lorem Picsum](https://picsum.photos)は、ダミー画像を提供するサービスです。ダミー画像のサイズが指定できるため、ウェブサイトのデザインやレイアウトのテストに便利です。
```

### 相対パスでの画像参照

ローカルファイルを参照する場合、相対パスを使用します。例えば、以下のようなフォルダー構成を考えます。

```
my_website
├── index.html
└── images
    └── example.png
```

`index.html`から`images/example.png`を参照する場合、以下のように記述します。

```html
<img src="images/example.png" alt="An example image" style="width: 300px; height: auto;">
```

## 文字装飾

### b要素とstrong要素

`<b>`要素は、テキストを太字にするために使用されます。

```html
<p>This is normal text and <b>this is bold text</b>.</p>
```

`<strong>`要素は、テキストを強調するために使用されます。通常、太字で表示されますが、意味的には重要な内容を示すために使用されます。

```html
<p>This is normal text and <strong>this is emphasized text</strong>.</p>
```

### i要素とem要素

`<i>`要素は、テキストを斜体にするために使用されます。

```html
<p>This is normal text and <i>this is italic text</i>.</p>
```

`<em>`要素は、テキストを強調するために使用されます。通常、斜体で表示されますが、意味的には強調すべき内容を示すために使用されます。

```html
<p>This is normal text and <em>this is emphasized text</em>.</p>
```

### small要素

`<small>`要素は、テキストを小さく表示するために使用されます。

```html
<p>This is normal text and <small>this is small text</small>.</p>
```

## リスト

### 番号付きリスト

`<ol>`要素は、番号付きリストを作成するために使用されます。各項目は`<li>`要素で表されます。

```html
<ol>
  <li>First item</li>
  <li>Second item</li>
  <li>Third item</li>
</ol>
```

### 箇条書きリスト

`<ul>`要素は、箇条書きリストを作成するために使用されます。各項目は`<li>`要素で表されます。

```html
<ul>
  <li>First item</li>
  <li>Second item</li>
  <li>Third item</li>
</ul>
```

## 引用

### blockquote要素

`<blockquote>`要素は、引用を示すために使用されます。

```html
法政大学の目的は、以下のとおりである。

<blockquote cite="https://www.hosei.ac.jp/hosei/daigakugaiyo/rinen/rinen/">
    <ol>
        <li>「自由と進歩」の精神と公正な判断力をもって、主体的、自立的かつ創造的に、新しい時代を構築する市民を育てる。</li>
        <li>学問の自由に基づき、真理の探究と「進取の気象」によって、学術の発展に寄与する。</li>
        <li>多様化する地球規模の課題を解決し、「持続可能な地球社会の構築」に貢献する。</li>
    </ol>
</blockquote>
```

### q要素

`<q>`要素は、短い引用を示すために使用されます。通常、引用符で囲まれます。

```html
<p><q>Anyone who has never made a mistake has never tried anything new.</q> - Albert Einstein</p>
```

### address要素

`<address>`要素は、連絡先情報を示すために使用されます。

```html
<address>
  3-7-2 Kajino-cho<br>
  Koganei-shi, Tokyo 184-8584<br>
  Japan
</address>
```

## Emoji

HTMLでは、Emojiを直接使用することができます。

```html
<p>Here is a grinning face: 😀</p>
```

以下ではいくつかの代表的なEmojiとそのコードを示します。

| Emoji | コード      |
| ----- | ----------- |
| 😀     | `&#128512;` |
| 😂     | `&#128514;` |
| ❤️     | `&#10084;`  |
| 🎉     | `&#127881;` |
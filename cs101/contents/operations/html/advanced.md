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

## b要素とstrong要素

`<b>`要素は、テキストを太字にするために使用されます。

```html
<p>This is normal text and <b>this is bold text</b>.</p>
```

`<strong>`要素は、テキストを強調するために使用されます。通常、太字で表示されますが、意味的には重要な内容を示すために使用されます。

```html
<p>This is normal text and <strong>this is emphasized text</strong>.</p>
```

## i要素とem要素

`<i>`要素は、テキストを斜体にするために使用されます。

```html
<p>This is normal text and <i>this is italic text</i>.</p>
```

`<em>`要素は、テキストを強調するために使用されます。通常、斜体で表示されますが、意味的には強調すべき内容を示すために使用されます。

```html
<p>This is normal text and <em>this is emphasized text</em>.</p>
```

## small要素

`<small>`要素は、テキストを小さく表示するために使用されます。

```html
<p>This is normal text and <small>this is small text</small>.</p>
```

## address要素

`<address>`要素は、連絡先情報を示すために使用されます。

```html

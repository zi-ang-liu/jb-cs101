# Selectors

## Selectorsの種類

| Selector Type      | Description                  | Example       |
| ------------------ | ---------------------------- | ------------- |
| Universal Selector | すべての要素を選択           | `*`           |
| Element Selector   | 特定のHTML要素を選択         | `h1`, `p`     |
| Grouping Selector  | 複数のセレクタをまとめて指定 | `h1, p`       |
| ID Selector        | 特定のIDを持つ要素を選択     | `#id-name`    |
| Class Selector     | 特定のクラスを持つ要素を選択 | `.class-name` |

## Universal Selector

Universal Selectorは、すべてのHTML要素にスタイルを適用します。

以下の例では、すべての要素に赤色の文字とArialフォントを適用しています。

```css
* {
    color: red;
    font-family: Arial;
}
```

HTML文書では、すべての要素にスタイルが適用されます。

```html
<h1>This is a heading</h1>
<p>This is a paragraph.</p>
```

## Element Selector

Element Selectorは、指定したHTML要素にスタイルを適用します。

以下の例では、`h1`, `p`要素にスタイルを適用しています。

```css
h1 {
    color: blue;
    font-size: 24px;
    background-color: lightgray;
}
p {
    color: red;
    font-size: 16px;
}
```

HTML文書では、`h1`と`p`要素にスタイルが適用されます。

```html
<h1>This is a heading</h1>
<p>This is a paragraph.</p>
```

## Grouping Selector

Grouping Selectorは、複数のセレクタをまとめて指定し、同じスタイルを適用します。

以下の例では、`h1`と`p`要素に同じスタイルを適用しています。

```css
h1, p {
    color: green;
    font-family: Verdana;
}
```

以下の書き方でも同じ効果があります。

```css
h1 {
    color: green;
    font-family: Verdana;
}
p {
    color: green;
    font-family: Verdana;
}
```

## id Selector

id Selectorは、特定のIDを持つ要素にスタイルを適用します。

```css
#header {
    color: green;
    font-size: 20px;
}
```

HTML文書では、そのIDを持つ要素にスタイルが適用されます。

```html
<h1 id="header">This is a header</h1>
<p>This is a paragraph.</p>
```

:::{note}
- IDはHTML文書内で一意である必要があります。
- IDの最初の文字は英字でなければなりません。
- IDは、CSSで`#id-name`の形式で、`#`で始まります。
:::

## Class Selector

Class Selectorは、特定のクラスを持つ要素にスタイルを適用します。

```css
.warning {
    color: orange;
    font-weight: bold;
}
```

HTML文書では、そのクラスを持つ要素にスタイルが適用されます。

```html
<h1 class="warning">This is a warning header</h1>
<p class="warning">This is a warning paragraph</p>
<p>This is a normal paragraph.</p>
```

:::{note}
- クラスはHTML文書内で複数回使用できます。
- クラスの最初の文字は英字でなければなりません。
- クラスは、CSSで`.class-name`の形式で、`.`で始まります。
:::


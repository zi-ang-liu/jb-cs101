# Selectors

## Selectorsの種類

| Selector Type      | Description                  | Example       |
| ------------------ | ---------------------------- | ------------- |
| Element Selector   | 特定のHTML要素を選択         | `h1`, `p`     |
| Class Selector     | 特定のクラスを持つ要素を選択 | `.class-name` |
| ID Selector        | 特定のIDを持つ要素を選択     | `#id-name`    |
| Universal Selector | すべての要素を選択           | `*`           |
| Grouping Selector  | 複数のセレクタをまとめて指定 | `h1, p`       |

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
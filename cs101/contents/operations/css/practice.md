# 実習

## 実習内容

以下の要件を満たすように、htmlとcssを使用して、個人のホームページや関心のあるテーマに関するウェブページを作成しましょう．

- HTMLファイルとCSSファイルを別々に作成すること
- HTMLファイルには、`<a>`，`<h1>`，`<h2>`，`<p>`などの基本的なHTML要素を使用すること
- CSSファイルには、`universal selector`，`class selector`を使用して、HTML要素にスタイルを適用すること

## 参考例（テンプレート）

参考例に基づくサイトを作成する場合は，HTMLの内容，CSSのスタイルを適宜変更して、個人の情報や関心のあるテーマに合わせてください．

最低限、以下の要件を満たすようにしてください．

- 画像を1つ以上使用すること．内容は自由で，テーマに合わせばよい．
- `skill`と`social`のセクション以外，もう一つセクションを追加すること．
- htmlファイルの内容を適宜変更すること．

### 参考例の構成

```plain text
my_website/
├── index.html
└── assets/
    └── images/
        └── profile.jpg
├── css/
    └── styles.css
```

### CSSファイル

```css
/* style.css */
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    font-family: 'Arial', sans-serif;
    background: #f0f2f5;
    color: #333;
}

.container {
    width: 800px;
    margin: 50px auto;
    background: #fff;
    padding: 30px;
    border-radius: 12px;
}

.header {
    text-align: center;
    margin-bottom: 30px;
}

.profile-image {
    width: 140px;
    height: 140px;
    border-radius: 50%;
    border: 3px solid #007acc;
    margin-bottom: 16px;
}

h1 {
    font-size: 2.2rem;
    color: #222;
}

.bio {
    font-size: 1rem;
    margin-top: 10px;
    color: #666;
}

.section {
    margin-top: 40px;
}

.section h2 {
    font-size: 1.3rem;
    color: #007acc;
    border-left: 5px solid #007acc;
    padding-left: 10px;
    margin-bottom: 15px;
}

.skills ul {
    list-style: none;
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
}

.skills li {
    background: #e6f2fb;
    padding: 8px 14px;
    border-radius: 20px;
    font-size: 0.95rem;
}

.social a {
    margin-right: 18px;
    color: #007acc;
    text-decoration: none;
    font-weight: bold;
    font-size: 0.95rem;
}

.social a:hover {
    color: #005f99;
    text-decoration: underline;
}
```

### HTMLファイル

```html
<!-- index.html -->
 <!DOCTYPE html>
<html lang="ja">

<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" href="css/styles.css">
    <title>法政 太郎 | ホームページ</title>
</head>

<body>
    <div class="container">
        <div class="header">
            <img src="assets/images/profile.jpg" alt="法政 太郎のプロフィール画像" class="profile-image" />
            <h1>法政 太郎</h1>
            <p class="bio">1年生...</p>
        </div>

        <div class="section">
            <h2>スキル</h2>
            <div class="skills">
                <ul>
                    <li>HTML</li>
                    <li>CSS</li>
                    <li>JavaScript</li>
                    <li>Python</li>
                </ul>
            </div>
        </div>

        <div class="section">
            <h2>リンク</h2>
            <div class="social">
                <a href="#">Email</a>
            </div>
        </div>
    </div>
</body>

</html>
```
# 生成AIの活用

## 生成AIとは

**生成AI**（generative artificial intelligence）とは，生成モデルを用いて，テキスト，画像，音声などのコンテンツを自動生成する人工知能の一種である．**生成モデル**（generative model）は，大量のデータを学習し，与えられた入力に対して新しいデータを生成する．

2022年11月にChatGPTが公開されたことで，生成AIは急速に普及し，個人や企業，研究機関などで広く利用されるようになった．これに続き，Microsoft Copilot，Claude，Geminiなど多くの生成AIが登場している．

| チャットボット    | 開発元    | 初版       |
| ----------------- | --------- | ---------- |
| ChatGPT           | OpenAI    | 2022年11月 |
| Microsoft Copilot | Microsoft | 2023年2月  |
| Claude            | Anthropic | 2023年3月  |
| Gemini            | Google AI | 2023年3月  |

:::{note}
**GPT**（Generative Pre-trained Transformer）は，OpenAIが開発した大規模言語モデルのシリーズである．GPT-1は，2018年に発表された論文「[Improving Language Understanding by Generative Pre-Training](https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf)」で紹介された．ChatGPTの公開当初はGPT-3（Generative Pre-trained Transformer 3）という大規模言語モデルを用いていた．
:::

## 生成AIの分類

生成AIは、出力の形式に基づいて以下のように分類できる。

- テキスト生成
- 画像生成
- 音声生成
- 動画生成

生成AIを活用することで，日常生活，ビジネス，研究，教育などの様々な場面で業務の効率化が可能となる．

## テキスト生成

テキスト生成は，生成AIの中でもよく利用されている分野である．テキスト生成の応用例としては，以下のようなものが挙げられる．

- 要約生成
- 文章生成
- 質問応答
- 翻訳
- データ分析
- プログラム生成   

:::{note}
**テキスト生成の難しさ**

英語アルファベットの26文字と空白文字からなる$n$文字の文章を生成する場合，$27^{n}$通りの組み合わせが考えられる．例えば，100文字の文章を生成する場合，$27^{100}$通りの組み合わせが存在し，このうち意味のある文章は極めて少ない．
:::

**練習問題**
- [ChatGPT](https://chatgpt.com/)にアクセスし，チャットボットと会話してみよう．
- `Hello, world!`と出力するC言語のプログラムをChatGPTに生成させてみよう．
- 本日の東京の天気をChatGPTに尋ねてみよう．


### プロンプトエンジニアリング

生成AIの分野において，**プロンプト**（prompt）とは，生成AIに与える入力データのことを指す．


<!-- - table, flowchart
- reverse question
- character setting, format, background
- few-shot
- conversation
- chain of reasoning thought
- meta-learning， meta-problem -->

## 画像生成

- [DALL-E 3](https://openai.com/index/dall-e-3/)


## 音声生成

- [Suno](https://suno.ai/)
- [SOUNDRAW](https://soundraw.io/)

## 動画生成

- [Sora](https://openai.com/sora/)

## Coding Assistant

- [GitHub Copilot](https://github.com/features/copilot)
- [Cursor](https://www.cursor.com/)

## 参考情報

- [大学・高専における生成AIの教学面の取扱いについて](https://www.mext.go.jp/b_menu/houdou/2023/mext_01260.html)，文部科学省
- [AIに関する暫定的な論点整理](https://www8.cao.go.jp/cstp/ai/ronten_honbun.pdf)，内閣府AI戦略会議
- [生成AIツールに対する基本的考え方](https://www.hoseikyoiku.jp/lf/back_news/view.php?c=topics_view&pk=1687401621)，法政大学
- [生成AIに関する注意点](https://www.tlsc.osaka-u.ac.jp/project/generative_ai/important_point.html)，大阪大学
- [生成AIの利用ガイドライン](https://www.jdla.org/document/#ai-guideline)，日本デイープラーニング協会
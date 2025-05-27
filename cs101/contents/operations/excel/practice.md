# 実習

## Irisデータセットを用いたExcelでのデータ分析と可視化

Irisデータセットは，研究者R.A. Fisherが1936年の論文「[The use of multiple measurements in taxonomic problems](https://doi.org/10.1111/j.1469-1809.1936.tb02137.x)」で使用されたデータセットです。現在では，機械学習やデータ分析の分野で広く使用されており，特に分類問題のベンチマークとして知られています。

Irisデータセットは，[kaggle](https://www.kaggle.com/datasets/uciml/iris)，[UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/iris)，[scikit-learn](https://scikit-learn.org/1.4/auto_examples/datasets/plot_iris_dataset.html)などで入手可能です。

このデータセットは，3種類のアヤメの花（Setosa，Versicolor，Virginica），それぞれ50標本の計150標本から構成されています。各標本は，萼と花弁の長さと幅を測定した4つの特徴量を持っています。

- sepal length: 萼の長さ
- sepal width: 萼の幅
- petal length: 花弁の長さ
- petal width: 花弁の幅

このデータセットは以下のようになっています。

| Id  | sepal_length | sepal_width | petal_length | petal_width | species        |
| --- | ------------ | ----------- | ------------ | ----------- | -------------- |
| 1   | 5.1          | 3.5         | 1.4          | 0.2         | Iris-setosa    |
| 2   | 4.9          | 3.0         | 1.4          | 0.2         | Iris-setosa    |
| 3   | 4.7          | 3.2         | 1.3          | 0.2         | Iris-setosa    |
| ... | ...          | ...         | ...          | ...         | ...            |
| 150 | 5.9          | 3.0         | 5.1          | 1.8         | Iris-virginica |

`Id`は各標本の識別子で，`species`はアヤメの種類を示しています。`sepal_length`，`sepal_width`，`petal_length`，`petal_width`は各標本の特徴量です。

以下リンクからExcel形式のIrisデータセットをダウンロードできます。

- [iris.xlsx](./data/iris.xlsx)

### 実習問題

本実習では，Irisデータセットを使用して，Excelを用いた計算およびグラフ作成を行います。得られた計算結果およびグラフをもとに，Word文書として考察を含むレポートを作成してください。

1. Setosa（標本1～50）の`sepal_length`に関する以下の統計量を求めよ．
   - 平均値
   - 中央値
   - 最大値
   - 最小値
   - `sepal_length`が`5.0`以上の標本の個数
2. Setosa（標本1～50）の`sepal_length`と`sepal_width`の相関関係を調べよ．
   - ヒント：散布図と相関係数を用いて調べること．
3. 三種類の花（Setosa，Versicolor，Virginica）の`petal_length`の分布を比較するため，箱ひげ図を作成せよ．

レポートのテンプレートは以下のリンクからダウンロードできます。

- [report_template.docx](./data/report_template.docx)

レポートの構成は以下のようにしてください。

- タイトル（「Irisデータセットを用いたExcelでのデータ分析と可視化」にする）
- 氏名，学籍番号
- 概要（100字程度）
- はじめに（Irisデータセットに関する紹介，生成AIを用いても良い）
- 実習内容
  - 実習1: 統計量の計算
  - 実習2: 相関関係の調査
  - 実習3: 箱ひげ図の作成
- 考察（実習結果に対する考察，生成AIは使用しないこと）
- おわりに
- 謝辞（必要に応じて。生成AIを使用した場合はその旨を記載すること）
- 参考文献（論文，Webページなど）
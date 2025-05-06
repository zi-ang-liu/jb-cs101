# 実習

## Irisデータセット

Irisデータセットは、研究者R.A. Fisherが1936年の論文「[The use of multiple measurements in taxonomic problems](https://doi.org/10.1111/j.1469-1809.1936.tb02137.x)」で使用されたデータセットです。現在では、機械学習やデータ分析の分野で広く使用されており、特に分類問題のベンチマークとして知られています。

- [kaggleのIrisデータセット](https://www.kaggle.com/datasets/uciml/iris)
- [UCI Machine Learning RepositoryのIrisデータセット](https://archive.ics.uci.edu/ml/datasets/iris)
- [scikit-learnのIrisデータセット](https://scikit-learn.org/1.4/auto_examples/datasets/plot_iris_dataset.html)

このデータセットは、3種類のアヤメの花（Setosa、Versicolor、Virginica）、それぞれ50標本の計150標本から構成されています。各標本は、萼と花弁の長さと幅を測定した4つの特徴量を持っています。

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

`Id`は各標本の識別子で、`species`はアヤメの種類を示しています。`sepal_length`、`sepal_width`、`petal_length`、`petal_width`は各標本の特徴量です。

以下リンクからデータセットをダウンロードできます。

- [iris.xlsx](./data/iris.xlsx)

### 実習問題
1. Setosa（標本1～50）の`sepal_length`について、平均値、中央値、最大値、最小値、標準偏差を求めてください。
2. Setosa（標本1～50）の`sepal_length`について、`5.0`以上の標本の数を求めてください。
3. Setosa（標本1～50）の`sepal_length`と`sepal_width`の相関関係を調べてください。
   - ヒント：相関関係を調べるために、散布図を作成し、相関係数を計算してください。
4. 三種類の花（Setosa、Versicolor、Virginica）の`petal_length`の分布を比較するために、箱ひげ図を作成してください。
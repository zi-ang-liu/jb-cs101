# コンピューターとは

**コンピューター**（computer）とは，電子回路を用い，指示された通り自動的に計算やデータ処理を行う装置で，**電子計算機**とも呼ばれる．**計算機**という言葉は，狭義では電子計算機を指すが，広義では計算を行う装置全般を指す．

コンピューターには，日常生活で使われるパソコン（パーソナルコンピュータ）をはじめ，スーパーコンピューター，スマートフォン，タブレットなど様々な種類がある．

:::{figure-md} Fugaku
<img src="./image/RIKEN_R-CCS_Fugaku.jpg" alt="富岳" width="300px">

日本のスーパーコンピューター「富岳（ふがく）」 © [Wikipedia](https://commons.wikimedia.org/wiki/File:RIKEN_R-CCS_Fugaku.jpg), [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/deed.en)
:::

## ハードウェアとソフトウェア

コンピューターは，**ハードウェア**（hardware）と**ソフトウェア**（software）から構成される．

ハードウェアは，コンピューターを構成する物理的な装置である．

ノイマン型アーキテクチャ（von Neumann architecture）は，今のほとんどのコンピューターの基盤となるアーキテクチャである．ノイマン型アーキテクチャでは，プログラムをハードウェアから独立して，データと同様に扱うことができる．このような考え方は**プログラム内蔵方式**（stored-program computer）と呼ばれる．

ノイマン型コンピューターは，以下の5つの主要な構成要素からなる．

- 演算装置（ALU: Arithmetic/Logic Unit，算術論理演算装置）
- 制御装置（Control Unit）
- 記憶装置（Memory Unit）
- 入力装置（Input Unit）
- 出力装置（Output Unit）

次の図では，ノイマン型アーキテクチャを示している．

:::{figure-md} VonNeumann
<img src="./image/Von_Neumann_Architecture.svg.png" alt="ノイマン型アーキテクチャ" width="300px">

ノイマン型アーキテクチャ 
:::

CPU（Central Processing Unit）は，演算装置と制御装置を含むコンピューターの中心的な部品である．
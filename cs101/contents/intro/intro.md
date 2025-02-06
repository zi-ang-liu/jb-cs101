# コンピューターとは

**コンピューター**（computer）とは，電子回路を用い，指示された通り自動的に計算やデータ処理を行う装置で，**電子計算機**とも呼ばれる．**計算機**という言葉は，狭義では電子計算機を指すが，広義では計算を行う装置全般を指す．

コンピューターには，日常生活で使われるパーソナルコンピュータをはじめ，スーパーコンピューター，スマートフォン，タブレットなど様々な種類がある．

:::{figure-md} Fugaku
<img src="./image/RIKEN_R-CCS_Fugaku.jpg" alt="富岳" width="300px">

日本のスーパーコンピューター「富岳（ふがく）」 © [Barsaka2](https://commons.wikimedia.org/wiki/File:RIKEN_R-CCS_Fugaku.jpg), [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/deed.en)
:::

パーソナルコンピュータ（パソコン，PC）は，一般的には，デスクトップPCとノート型PCに分けられる．

## ハードウェアとソフトウェア

コンピューターは，**ハードウェア**（hardware）と**ソフトウェア**（software）から構成される．ここからは，ハードウェアとソフトウェアについて説明する．

### ハードウェア

ハードウェアとは，コンピューターを構成する物理的な装置である．

ノイマン型アーキテクチャ（von Neumann architecture）は，今のほとんどのコンピューターの基盤となるアーキテクチャである．次の図では，ノイマン型アーキテクチャを示している．

:::{figure-md} VonNeumann
<img src="./image/VonNeumann.svg" alt="ノイマン型アーキテクチャ" width="300px">

ノイマン型アーキテクチャ 
:::

図に示すように，ノイマン型コンピューターは，以下の5つの構成要素からなる．

- 演算装置（Arithmetic/Logic Unit）
- 制御装置（Control Unit）
- 記憶装置（Memory Unit）
- 入力装置（Input Unit）
- 出力装置（Output Unit）

**演算装置**は，算術演算と論理演算を行う装置である．**制御装置**は，他の装置（演算装置，記憶装置，入出力装置）を制御する装置である．演算装置と制御装置を統合したものを**中央処理装置**（Central Processing Unit, CPU）と呼ぶ．CPUは，コンピューターの中心的な役割を果たし，コンピューターの頭脳とも呼ばれる．下の図は，2024年10月から発売されているIntel Core UltraシリーズのCPUである．

:::{figure-md} intel_ultra
<img src="./image/intel_ultra.png" alt="Intel Core Ultra" width="300px">

Intel Core Ultra © [ZMASLO](https://www.youtube.com/@ZMASLO)
:::

**記憶装置**は，データやプログラムを保存するための装置である．記憶装置には，**主記憶装置**（Main Memory）と**補助記憶装置**（Secondary Memory）がある．主記憶装置は，CPUから直接アクセスできる高速な記憶装置である．補助記憶装置は，主記憶装置よりも大容量で，主記憶装置よりも遅いが，データを永続的に保存できる．

:::{note}
ノイマン型アーキテクチャでは，プログラムをハードウェアから独立して，データと同様に扱うことができる．このような考え方は**プログラム内蔵方式**（stored-program computer）と呼ばれる．
:::

### ソフトウェア

ソフトウェアとは，コンピューターを利用するためのプログラムの総称である．一般的に，ソフトウェアは，システムソフトウェアとアプリケーションソフトウェアに分類される．

特定の仕事をするために作成されたソフトウェアを**アプリケーションソフトウェア**（application software）と呼ぶ．ワードプロセッサ，表計算ソフト，電子ゲームなどがアプリケーションソフトウェアの例である．

**システムソフトウェア**（system software）は，コンピューターのハードウェアを制御や管理するためのソフトウェアである．よく知られているシステムソフトウェアとして，**オペレーティングシステム**（operating system, OS）がある．Microsoft Windows，macOS，Linux，Androidなどがオペレーティングシステムの例である．

:::{figure-md} ハードウェアとソフトウェア
<img src="./image/hardware_software.svg" alt="ハードウェアとソフトウェア" width="200px">

ハードウェアとソフトウェア
:::

## 用語

| 略称 | 意味                    | 日本語訳                 |
| ---- | ----------------------- | ------------------------ |
| CPU  | Central Processing Unit | 中央処理装置             |
| OS   | Operating System        | オペレーティングシステム |
| PC   | Personal Computer       | パーソナルコンピュータ   |
| RAM  | Random Access Memory    | ランダムアクセスメモリ   |
| ROM  | Read-Only Memory        | 読み取り専用メモリ       |
| ALU  | Arithmetic/Logic Unit   | 演算論理装置             |
| CU   | Control Unit            | 制御装置                 |
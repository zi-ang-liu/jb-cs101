# ブール演算

コンピューターでは，すべての情報を0または1で表現する．このような情報を**ビット**（bit）と呼ぶ．ビットは，**binary digit**の混成語である．また，ビットは情報量の最小単位である．一桁のビットは，0または1のどちらかの値を取る．

ビットは一般的に0または1と表現されるが，FalseまたはTrueという**真理値**としての表現もよく使われる．

以下のC言語のコードは，`2 > 1`が真であり、`1`を出力する．`2 < 1`が偽であり、`0`を出力する．

```c
#include <stdio.h>

int main() {  
  printf("%d\n", 2 > 1); // 1
  printf("%d\n", 2 < 1); // 0
  return 0;
}
```

Pythonでは，`True`と`False`を使って真理値を表現する．

```python
print(2 > 1)  # True
print(2 < 1)  # False
```

このような真理値（0と1）を扱うための数学的な体系を**ブール代数**（Boolean algebra）と呼ぶ．ブール代数は，イギリスの数学者ジョージ・ブール（George Boole）によって考案された．ブール演算は，AND，OR，NOT，XORなどの論理演算子を使って真偽値を操作する．

## ゲート

コンピューターでは，**ゲート**（gate，論理ゲート，logic gate）と呼ばれる装置を使ってブール演算を実行する．ゲートは，一つまたは複数の入力信号を受け取り，それらの信号を処理して出力信号を生成する．

ここでは，以下の4つの基本的な論理ゲートを紹介する．

- AND
- OR
- NOT
- XOR

これらのゲートをの紹介には，論理式，真理値表，MIL記号を使う．

**論理式**（Boolean expressions）は，数学記号を使って，数式で真理値の演算を表現する．**真理値表**（truth table）は，ゲートのすべての入力組み合わせに対して，出力の真理値を示す表である．**MIL記号**（MIL symbols）は，論理ゲートを図で表現するための記号である．

### ORゲート

$p$と$q$を真理値とするとき，$p$と$q$の論理和（logical disjunction）は，$p \lor q$と書く．その真理値表は以下の通りである．

| $p$ | $q$ | $p \lor q$ |
| --- | --- | ---------- |
| 0   | 0   | 0          |
| 0   | 1   | 1          |
| 1   | 0   | 1          |
| 1   | 1   | 1          |

論理和の演算では，$p$または$q$のどちらかが$1$（真）のとき，出力が$1$（真）となる．

論理和の演算を行うORゲートは次のようにMIL記号で表現される．

:::{figure-md} or_gate
<img src="https://upload.wikimedia.org/wikipedia/commons/1/16/OR_ANSI_Labelled.svg" alt="OR Gate" width="200px">

ORゲート
:::

C言語では、論理和の演算は`||`演算子を使って表現される．例えば、`p || q`は、$p$または$q$のいずれかが真である場合に真を返す．

```c
#include <stdio.h>
int main() {
    int p = 1; // 真
    int q = 0; // 偽
    printf("p OR q = %d\n", p || q); // 出力: 1
    return 0;
}
```

### ANDゲート

$p$と$q$を真理値とするとき，$p$と$q$の**論理積**（logical conjunction）は，$p \land q$と書く．その真理値表は以下の通りである．

| $p$ | $q$ | $p \land q$ |
| --- | --- | ----------- |
| 0   | 0   | 0           |
| 0   | 1   | 0           |
| 1   | 0   | 0           |
| 1   | 1   | 1           |

論理和の演算では，$p$が$1$（真）でかつ$q$が$1$（真）のときだけ，出力が$1$（真）となる．

論理和の演算を行うANDゲートは次のようにMIL記号で表現される．

:::{figure-md} and_gate
<img src="https://upload.wikimedia.org/wikipedia/commons/b/b9/AND_ANSI_Labelled.svg" alt="AND Gate" width="200px">

ANDゲート
:::

C言語では、論理積の演算は`&&`演算子を使って表現される．例えば、`p && q`は、$p$と$q$の両方が真である場合に真を返す．

```c
#include <stdio.h>
int main() {
    int p = 1; // 真
    int q = 0; // 偽
    printf("p AND q = %d\n", p && q); // 出力: 0
    return 0;
}
```

### NOTゲート

$p$を真理値とするとき，$p$の**否定**（logical negation）は，$\lnot p$と書く．その真理値表は以下の通りである．

| $p$ | $\lnot p$ |
| --- | --------- |
| 0   | 1         |
| 1   | 0         |

否定の演算では，入力が$1$（真）のとき，出力が$0$（偽）となり，入力が$0$（偽）のとき，出力が$1$（真）となる．

否定の演算を行うNOTゲートは次のようにMIL記号で表現される．

:::{figure-md} not_gate
<img src="https://upload.wikimedia.org/wikipedia/commons/6/60/NOT_ANSI_Labelled.svg" alt="NOT Gate" width="200px">

NOTゲート
:::

C言語では、否定の演算は`!`演算子を使って表現される．例えば、`!p`は、$p$が真である場合に偽を返し、$p$が偽である場合に真を返す．

```c
#include <stdio.h>
int main() {
    int p = 1; // 真
    printf("NOT p = %d\n", !p); // 出力: 0
    return 0;
}
```

### XORゲート

$p$と$q$を真理値とするとき，$p$と$q$の**排他的論理和**（exclusive or）は，$p \oplus q$と書く．その真理値表は以下の通りである．

| p   | q   | p XOR q |
| --- | --- | ------- |
| 0   | 0   | 0       |
| 0   | 1   | 1       |
| 1   | 0   | 1       |
| 1   | 1   | 0       |

排他的論理和の演算では，$p$と$q$のどちらか一方が$1$（真）のときだけ，出力が$1$（真）となる．

排他的論理和の演算を行うXORゲートは次のようにMIL記号で表現される．

:::{figure-md} xor_gate
<img src="https://upload.wikimedia.org/wikipedia/commons/1/17/XOR_ANSI_Labelled.svg" alt="XOR Gate" width="200px">
XORゲート
:::

### 記号まとめ

| 記号     | 意味 | C言語演算子 | Python演算子 |
| -------- | ---- | ----------- | ------------ |
| $\land$  | AND  | `&&`        | `and`        |
| $\lor$   | OR   | `\|\|`      | `or`         |
| $\lnot$  | NOT  | `!`         | `not`        |
| $\oplus$ | XOR  | `^`         | `^`          |

### やってみよう

ユーザーから2つの真理値（0または1）を入力として受け取り、AND、OR、NOT、XORの演算結果を表示するC言語のプログラムを作成してみよう。

#### 解答例

```c
#include <stdio.h>

int main() {
    int p, q;
    printf("Please enter p and q, where p and q are either 0 or 1.\n");
    printf("Enter p: ");
    scanf("%d", &p);
    printf("Enter q: ");
    scanf("%d", &q);
    printf("p = %d, q = %d\n", p, q);

    printf("*** Logical Operations ***\n");
    printf("p AND q = %d\n", p && q);
    printf("p OR q = %d\n", p || q);
    printf("NOT p = %d\n", !p);
    printf("p XOR q = %d\n", p ^ q);
    return 0;
}
```

## フリップフロップ

## 練習問題
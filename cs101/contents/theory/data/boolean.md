# ブール演算

コンピューターでは，すべての情報を0または1で表現する．このような情報を**ビット**（bit）と呼ぶ．ビットは，**binary digit**の混成語である．また，ビットは情報量の最小単位である．一桁のビットは，0または1のどちらかの値を取る．

ビットは一般的に0または1と表現されるが，FalseまたはTrueという**真理値**としての表現もよく使われる．

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

### ANDゲート




| p   | q   | p AND q | p OR q | NOT p | p XOR q |
| --- | --- | ------- | ------ | ----- | ------- |
| 0   | 0   | 0       | 0      | 1     | 0       |
| 0   | 1   | 0       | 1      | 1     | 1       |
| 1   | 0   | 0       | 1      | 0     | 1       |
| 1   | 1   | 1       | 1      | 0     | 0       |

## 記号

| 記号     | 意味 |
| -------- | ---- |
| $\land$  | AND  |
| $\lor$   | OR   |
| $\lnot$  | NOT  |
| $\oplus$ | XOR  |

### やってみよう

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
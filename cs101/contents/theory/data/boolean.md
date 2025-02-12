# ブール演算

コンピューターでは、すべての情報を0または1で表現する。このような情報を**ビット**（bit）と呼ぶ。また，ビットは情報量の最小単位である。一桁のビットは、0または1のどちらかの値を取る。

:::{note}
ビットは、**binary digit**の混成語である。
:::

ビットは一般的に0または1と表現されるが，FalseまたはTrueという**真偽値**としての表現もよく使われる。このような真偽値を扱うための数学的な体系を**ブール代数**（Boolean algebra）と呼ぶ。

:::{note}
ブール代数は，19世紀の数学者ジョージ・ブール（George Boole）によって考案された。
:::

## ゲート

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
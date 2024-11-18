# ブール演算

ブール演算（Boolean operation）

### ゲート

| p   | q   | p AND q | p OR q | NOT p | p XOR q |
| --- | --- | ------- | ------ | ----- | ------- |
| 0   | 0   | 0       | 0      | 1     | 0       |
| 0   | 1   | 0       | 1      | 1     | 1       |
| 1   | 0   | 0       | 1      | 0     | 1       |
| 1   | 1   | 1       | 1      | 0     | 0       |

### 記号

| 記号     | 意味 |
| -------- | ---- |
| $\land$  | AND  |
| $\lor$   | OR   |
| $\lnot$  | NOT  |
| $\oplus$ | XOR  |

#### やってみよう

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

### フリップフロップ

## 練習問題
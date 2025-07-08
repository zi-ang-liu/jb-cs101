# アルゴリズム

```{epigraph}
Today, computer science has established itself as the science of algorithms.

-- G. Brookshear and D. Brylow, Computer Science: An Overview, 13th ed. Pearson, 2018.
```

## 学習目標

- アルゴリズムの概念を理解する。
- 代入、選択構造、反復構造を理解し、擬似コードで表現できる。
- 簡単な問題に対して、アルゴリズムを設計し、擬似コードで表現できる。

## アルゴリズムとは

**アルゴリズム**（algorithm）とは、問題を解決するための手順を指す。

今までは、いくつかのアルゴリズムを紹介してきた。

CPUが以下の命令サイクルと呼ばれる手順を繰り返すだけで、コンピューターは動作する。

1. **命令の取得**（fetch）：メモリから次の命令を取得する。
2. **命令の解読**（decode）：取得した命令を解読する。
3. **命令の実行**（execute）：解読した命令を実行する。

また、10進数から他の記数法への変換は、下記の手順で行うことができる：

1. 与えられた値を底で割り、商と余りを求める。
2. 商が0になるまで繰り返す。
3. 商が0になったら、余りを逆順に並べる。

## 擬似コード

擬似コード（Pseudocode）は、アルゴリズムを記述するための表記法である。厳密な構文はないが、自然言語より明確にアルゴリズムを表現できる。

### 代入

代入（assignment）とは、変数に値を設定する操作である。擬似コードでは、以下のように表現される：

$$
\texttt{sum} \gets 0
$$

変数$\texttt{sum}$に0を代入することを意味する。

他には、以下のように表現することもできる：

$$
\texttt{sum} = 0
$$

$$
\text{Set } \texttt{sum} \text{ to } 0
$$

式を代入することもできる：

$$
\texttt{sum} \gets \texttt{salary} + \texttt{bonus}
$$

```python
salary = 400
bonus = 100
sum = salary + bonus
print(sum)
```

```c
#include <stdio.h>
int main() {
    int salary = 400;
    int bonus = 100;
    int sum = salary + bonus;
    printf("%d\n", sum);
    return 0;
}
```

### 選択構造

選択構造（selection structure）は、条件に基づいて異なる処理を実行するための構造である。擬似コードでは、以下のように表現される：

```{prf:algorithm} selection-structure
:label: selection-structure

1. **if** condition **then**
   1. activity
2. **else**
   1. activity
```

例えば、

```{prf:algorithm} score-evaluation
:label: score-evaluation

1. **if** score >= 60 **then**
    1. print("合格")
2. **else**
    1. print("不合格")
```

```python
score = 75
if score >= 60:
    print("Pass")
else:
    print("Fail")
```

```c
#include <stdio.h>
int main() {
    int score = 75;
    if (score >= 60) {
        printf("Pass\n");
    } else {
        printf("Fail\n");
    }
    return 0;
}
```


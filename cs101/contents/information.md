# 情報の表現

- [情報の表現](#情報の表現)
  - [ビット](#ビット)
  - [文字コード](#文字コード)
    - [ASCII](#ascii)
      - [Example: "Hello." をASCIIコードで表現する](#example-hello-をasciiコードで表現する)
      - [やってみよう](#やってみよう)
    - [Unicode](#unicode)


## ビット

ビット (bit) 

binary digitの混成語

## 文字コード

### ASCII

ASCII（American Standard Code for Information Interchange、アスキーと読む）

7ビットのパターンを使って、文字を表現する。
* 英語のアルファベット
* 数字
* 一部の記号
* 制御文字（改行、タブなど）

7ビットのパターンで表現できる文字は128文字である。

$$
2^7 = 128
$$

左端に1ビットの0を追加して、8ビットパターンの記号へ拡張され、1バイトのメモリを使って文字を表現する。

ASCII印字可能文字は[こちら](https://ja.wikipedia.org/wiki/ASCII)

#### Example: "Hello." をASCIIコードで表現する

"Hello." をASCIIコードで表現すると、次のようになる。

| 文字 | ビットパターン | 10進数 |
| ---- | -------------- | ------ |
| H    | 0100 1000      | 72     |
| e    | 0110 0101      | 101    |
| l    | 0110 1100      | 108    |
| l    | 0110 1100      | 108    |
| o    | 0110 1111      | 111    |
| .    | 0010 1110      | 46     |

#### やってみよう

```c
#include <stdio.h>

int main() {
    char hello[] = "Hello.";
    for (int i = 0; i < 6; i++) {
        printf("%c: %d\n", hello[i], hello[i]);
    }
    return 0;
}
```

### Unicode

16ビットを使って、65536個の文字を表現する。

$$
2^{16} = 65536
$$



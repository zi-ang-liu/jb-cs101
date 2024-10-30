# ネットワークとインターネット

## OSI参照モデルとTCP/IPモデル

OSI参照モデル
1. 物理層
2. データリンク層
3. ネットワーク層
4. トランスポート層
5. セッション層
6. プレゼンテーション層
7. アプリケーション層

インターネット・プロトコル・スイート（TCP/IPモデル）
1. リンク層
2. インターネット層
3. トランスポート層
4. アプリケーション層

## LAN

LAN（Local Area Network）

狭い範囲にあるコンピュータやネットワーク機器を接続するネットワーク
- 学校、工場、オフィス、家庭など

LANのトポロジー：バス型、スター型、リング型

スター型：ハブ

### イーサネット（Ethernet）

トポロジー：バス型とスター型、多くがスター型

OSI参照モデル：物理層、データリンク層

アクセス制御方式（access control method）：CSMA/CD（Carrier Sense Multiple Access with Collision Detection）

MAC（Media Access Control）アドレス：48ビットの識別番号

転送速度は当初10Mbpsだったが、100Mbps、1Gbps、10Gbpsと進化

### 無線LAN

## WAN

WAN（Wide Area Network）

インターネットサービスポロバイダ（ISP, Internet Service Provider）

代表的なISP
- au one net
- J:COM
- OCN

## インターネット

インターネット（the Internet）

intra（内部） + net（ネットワーク）: 異なるネットワークを相互に接続するネットワーク

組織のネットワークやISPなどが相互に接続したネットワーク

アドレスの割付機関：ICANN（Internet Corporation for Assigned Names and Numbers）

プロトコルの制定機関：IETF（Internet Engineering Task Force）

## プロトコル

プロトコル（protocol）

TCP/IP
| 層                 | プロトコル                              |
| :----------------- | :-------------------------------------- |
| アプリケーション層 | HTTP, SMTP, POP3, FTP, Telnet, SSH, DNS |
| トランスポート層   | TCP, UDP                                |
| インターネット層   | IP, ICMP, ARP, RARP                     |
| リンク層           | Ethernet, Wi-Fi                         |
# CUIの基本操作

**CUI**（Character User Interface）とは、キーボードからコンピューターに文字列を入力して操作する体系・方法のことです。CUIは、GUI（Graphical User Interface）の対義語として使われることが多いです。

CUIと関連する概念として、**CLI**（Command Line Interface）があります。CLIは、コマンドラインを使ってコンピューターを操作するインターフェースのことです。コマンドラインも文字列であるため、CLIはCUIの一種と言えます。日本では、CUIの方が一般的ですが、英語圏ではCLIが主流です。

CUIと比べて、CLIの学習コストは高いですが、CLIを使うことで、より高度な操作が可能になります。

**コマンドプロンプト**（Command Prompt, also known as cmd.exe）は、Windowsにおける代表的なCLIの一つです。cmd.exeの後継として、**PowerShell**があり、より高度な操作が可能です。

ここではPowerShellの基本的な使い方を学びます。

## PowerShellの起動

PowerShellを起動するには、検索ボックスに「PowerShell」と入力し、検索結果から「Windows PowerShell」をクリックします。

## バージョン

PowerShellを起動したら、次のコマンドを入力して、<kbd>Enter</kbd> キーを押すことで、バージョンを確認できます。

```powershell
$PSVersionTable
```

PSVersion の値が5.1以下の場合、以下のサイトの手順に従って、PowerShell 5.1 以上にアップデートしてください。

- [https://learn.microsoft.com/ja-jp/powershell/scripting/install/installing-powershell-on-windows](https://learn.microsoft.com/ja-jp/powershell/scripting/install/installing-powershell-on-windows)


<div align="center">

![Python version](https://img.shields.io/badge/python-3.8+-important)
</div>

# SaliencyMap — in Python
## 概要  
顕著性マップを表示するデモアプリです。  
私は画像処理についてはまだ初心者ですが、興味を持っています。  
> **技術的なお話**  
> opencv-contribパッケージの`cv2.saliency.StaticSaliencySpectralResidual`を呼び出すラッパーアプリです。  

## システム要件  
- 必要ディスク容量：500MB(Pythonを含みません)  
- [Python](https://www.python.org/downloads/)をリンク先からダウンロードしてください。  

## 導入方法  
### 1. セットアップ  
- 以下のファイルをダブルクリックします。  
~~~
01-installation.bat
~~~
### 2. 実行  
1. 以下のファイルをダブルクリックします。  
~~~
run.bat
~~~
2. 実行するとブラウザが起動し[http://127.0.0.1:9999](http://127.0.0.1:9999)を開きます。  
> **NOTE**  
> デフォルトポート番号は、9999です。  
> アプリが起動せずポート番号を変更する時は、メモ帳で`run.bat`を開きの以下行の9999を別の数字(8888)などに変更し保存してください。  
> python src\launch.py --server_port 9999  
> REM 変更後  
> python src\launch.py --server_port 8888  

## 補足事項  
- ローカルで処理が完結します。画像を外部には送信しません。  

## Uninstall  
このアプリをアンインストールするには、以下の手順に従ってください。  
- アプリのフォルダをフォルダ毎削除してください。  
- アプリで処理した画像ファイルが一時フォルダに残ります。不要な場合は削除をお願いします。  
	- 一時フォルダの場所  
	パソコンの画面左下の「検索するには、ここに入力します」に以下をコピペしてEnterを押します。  
	~~~
	C:\Users\%USERNAME%\AppData\Local\Temp\gradio
	~~~
	
## Source code License.  
[MIT License](LICENSE)  

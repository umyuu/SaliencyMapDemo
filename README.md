---
license: mit
title: SaliencyMapDemo
sdk: gradio
emoji: 📊
colorFrom: yellow
colorTo: yellow
pinned: false
---
# 📖 SaliencyMap — in Python
![Python version](https://img.shields.io/badge/python-3.9+-important)
<a href="https://colab.research.google.com/github/umyuu/SaliencyMapDemo/blob/main/scripts/launch_app.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

## 📝 概要  
画像における注目すべき領域を可視化する「顕著性マップ」を表示するデモアプリです。  
私は画像処理についてはまだ初心者ですが、この技術に興味があります。  
本アプリは、opencv-contribパッケージの`cv2.saliency.StaticSaliencySpectralResidual`を関数を実行するラッパーアプリです。  

## 🚀 使い方  
### a. Google Colabで実行  
<a href="https://colab.research.google.com/github/umyuu/SaliencyMapDemo/blob/main/scripts/launch_app.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>をクリックして、簡単に実行できます。  

### b. アプリをダウンロードして実行  
#### 💻 システム要件  
- 必要ディスク容量：500MB(Pythonを含みません)  
- Python のダウンロード:https://www.python.org/downloads/  

#### 📥 導入方法  
##### 1. セットアップ  
1. [Releases](/releases)ページを開き、一番上の `Assets` 欄にある `Source code (zip)` をダウンロードして展開します。  
2. `01-installation.bat`ファイルをダブルクリックします。  
##### 2. 実行  
`run.bat`ファイルをダブルクリックします。  
ブラウザが自動起動し、http://127.0.0.1:9999 にアクセスできます。  

**🔧 トラブルシューティング**  
- アプリが起動しない場合  
	既定のポート番号 (9999) が使用されている可能性があります。  
	メモ帳で `run.bat` ファイルを開き、以下の行の `9999` を別の数字 (例: 8888) に変更して上書き保存します。  
	~~~
	python app.py --server_port 9999  
	~~~
	変更後:
	~~~
	python app.py --server_port 8888  
	~~~
##### 💡 補足事項  
- アプリをダウンロードして実行の場合は、画像処理はローカル環境で行われます。画像は外部に送信されません。  

##### 🗑️ アンインストール  
以下の手順でアンインストールできます。  
1. アプリのフォルダを丸ごと削除します。  
2. アプリで処理した画像は一時フォルダに残ります。不要な場合は削除してください。  
	- 一時フォルダの場所  
	パソコンの画面左下の「検索するには、ここに入力します」に以下をペーストして Enter キーを押します。  
	~~~
	C:\Users\%USERNAME%\AppData\Local\Temp\gradio
	~~~

## 🤝 コントリビューターガイドライン  
[CONTRIBUTING](docs/CONTRIBUTING.md)  

## 📜 Source code License.  
[MIT License](LICENSE)  

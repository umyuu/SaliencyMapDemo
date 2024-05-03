# saliencymap
## Introduction  
gradioを使って、opencv-contribパッケージのcv2.saliency.StaticSaliencySpectralResidualを呼び出すサンプルプログラムです。  
私は画像処理についてはまだ初心者ですが、興味を持っています。  
以下から導入方法です。  

## 1. 仮想環境(venv)に必要ライブラリのインストール  
- リポジトリ直下にある以下のバッチを実行する。  
	~~~
	01-installation.bat
	~~~
	> **NOTE**  
	仮想環境の名称は「venv」で作成します。  

## 2. 実行  
- リポジトリ直下にある以下のバッチを実行する。  
	~~~
	run.bat
	~~~
	> **NOTE**  
	> デフォルトポートは9999です。  
	> 他のポート番号例えば8888に変更したい場合は、run.bat内の以下の行を書き換えてください。  
	> python src\app.py --server_port 8888  

## Source code License.  
[MIT License](LICENSE)  
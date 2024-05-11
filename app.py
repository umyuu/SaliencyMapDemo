# -*- coding: utf-8 -*-
"""
    SaliencyMapDemo
"""
import argparse
from datetime import datetime

from utils import get_package_version, Stopwatch
from reporter import get_current_reporter

def main():
	"""
		エントリーポイント
		1, コマンドライン引数の解析を行います
		2, アプリを起動します。
	"""
	log = get_current_reporter()
	log.info("#アプリ起動中")
	watch = Stopwatch.startNew()
	
	import app

	parser = argparse.ArgumentParser(prog=app.PROGRAM_NAME, description="SaliencyMapDemo")
	parser.add_argument('--server_port', type=int, default=9999, help="Gradio server port")
	parser.add_argument('--max_file_size', type=int, default=20 * 1024 * 1024, help="Gradio max file size")
	parser.add_argument('--version', action='version', version=f'%(prog)s {get_package_version()}')
	
	app.run(parser.parse_args(), watch)

if __name__ == "__main__":
    main()

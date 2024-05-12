# -*- coding: utf-8 -*-
"""
    SaliencyMapDemo
"""
from argparse import ArgumentParser, BooleanOptionalAction

import src.utils as utils
from src.reporter import get_current_reporter
        
PROGRAM_NAME = 'SaliencyMapDemo'
__version__ = utils.get_package_version()

def main():
    """
        エントリーポイント
        1, コマンドライン引数の解析を行います
        2, アプリを起動します。
    """
    log = get_current_reporter()
    log.info("#アプリ起動中")
    watch = utils.Stopwatch.startNew()
    
    from src.myapp import runApp

    parser = ArgumentParser(prog=PROGRAM_NAME, description="SaliencyMapDemo")
    parser.add_argument('--server_port', type=int, default=7860, help="Gradio server port")
    parser.add_argument('--max_file_size', type=int, default=20 * 1024 * 1024, help="Gradio max file size")
    parser.add_argument('--inbrowser',  action=BooleanOptionalAction, default=True, help="Gradio inbrowser")
    parser.add_argument('--share', action=BooleanOptionalAction, default=False, help="Gradio share")
    parser.add_argument('--version', action='version', version=f'%(prog)s {__version__}')
    
    args = parser.parse_args()
    
    runApp(args, watch)

if __name__ == "__main__":
    main()

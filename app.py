# -*- coding: utf-8 -*-
"""
    SaliencyMapDemo
"""
from argparse import ArgumentParser, BooleanOptionalAction

from src.utils import get_package_version
from src.myapp import run_app

PROGRAM_NAME = 'SaliencyMapDemo'
__version__ = get_package_version()


def main():
    """
        エントリーポイント
        1, コマンドライン引数の解析を行います
        2, アプリを起動します。
    """
    parser = ArgumentParser(prog=PROGRAM_NAME, description="SaliencyMapDemo")
    parser.add_argument('--inbrowser',
                        action=BooleanOptionalAction, default=True, help="Gradio inbrowser")
    parser.add_argument('--share',
                        action=BooleanOptionalAction, default=False, help="Gradio share")
    parser.add_argument('--server_port',
                        type=int, default=7860, help="Gradio server port")
    parser.add_argument('--max_file_size',
                        type=str, default="20MB", help="Gradio max file size")
    parser.add_argument('--version', action='version', version=f'%(prog)s {__version__}')

    args = parser.parse_args()
    run_app(args)


if __name__ == "__main__":
    main()

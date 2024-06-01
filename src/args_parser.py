# -*- coding: utf-8 -*-
"""コマンドライン引数の解析"""
from argparse import ArgumentParser, BooleanOptionalAction
from src import PROGRAM_NAME, get_package_version


def parse_args():
    """
    コマンドライン引数の解析を行います
    """
    parser = ArgumentParser(prog=PROGRAM_NAME, description=PROGRAM_NAME)
    parser.add_argument('--inbrowser',
                        action=BooleanOptionalAction, default=True, help="Gradio inbrowser")
    parser.add_argument('--share',
                        action=BooleanOptionalAction, default=False, help="Gradio share")
    parser.add_argument('--server_port',
                        type=int, default=7860, help="Gradio server port")
    parser.add_argument('--max_file_size',
                        type=str, default="20MB", help="Gradio max file size")
    parser.add_argument('--version', 
                        action='version', version=f'%(prog)s {get_package_version()}')

    return parser.parse_args()

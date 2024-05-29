# -*- coding: utf-8 -*-
"""
    Reporter
    ログハンドラーが重複登録されるのを防ぐために1箇所で生成してログハンドラーを返します。
    Example:
        from src.reporter import log

        log.info("message")
        # 2024-05-24T12:34:56+0900#アプリ起動中
"""
import json
from logging import Logger, getLogger
import logging.config
from typing import Optional

from . import PROGRAM_NAME


class Reporter:
    """
    シングルトンパターンを適用したロガークラス。
    このクラスのインスタンスがまだ存在しない場合は新たに作成し、既に存在する場合はそのインスタンスを返します。
    @see https://docs.python.jp/3/howto/logging-cookbook.html
    """
    _instance: Optional[Logger] = None  # Reporterクラスの唯一のインスタンスを保持します。

    def __new__(cls):
        """
        """
        # インスタンスがまだ存在しない場合は新たに作成します。
        if not cls._instance:
            logger = getLogger(PROGRAM_NAME)  # ロガーを取得します。
            with open(r'config.json', 'r', encoding='utf-8') as f:
                config = json.load(f)
            logging.config.dictConfig(config)
            cls._instance = logger  # 作成したロガーを保持します。
        return cls._instance  # 作成したまたは既存のロガーを返します。


log: Logger = Reporter()  # Reporterクラスのインスタンスを取得します。


def main():
    """
        Entry Point
    """
    log.debug("main")


if __name__ == "__main__":
    main()

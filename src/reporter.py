# -*- coding: utf-8 -*-
"""
    Reporter
    ログハンドラーが重複登録されるのを防ぐために1箇所で生成してログハンドラーを返します。
    Example:
        from reporter import get_current_reporter

        logger = get_current_reporter()
        logger.info("message");
"""
from logging import Logger, getLogger, Formatter, StreamHandler
from logging import DEBUG

_reporters = []


def get_current_reporter() -> Logger:
    """
    シングルトン
    """
    return _reporters[-1]


def __make_reporter(name: str = 'SaliencyMapDemo') -> None:
    """
    ログハンドラーを生成します。
    @see https://docs.python.jp/3/howto/logging-cookbook.html

    Parameters:
        name: アプリ名
    """
    handler = StreamHandler()  # コンソールに出力します。
    formatter = Formatter('%(asctime)s%(message)s')
    handler.setFormatter(formatter)
    handler.setLevel(DEBUG)

    logger = getLogger(name)
    logger.setLevel(DEBUG)
    logger.addHandler(handler)
    _reporters.append(logger)


__make_reporter()


def main():
    """
        Entry Point
    """
    assert len(_reporters) == 1

    logger = get_current_reporter()
    logger.debug("main")


if __name__ == "__main__":
    main()

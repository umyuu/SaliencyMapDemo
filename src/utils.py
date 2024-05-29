# -*- coding: utf-8 -*-
"""ユーティリティ"""
import time


def get_package_version() -> str:
    """
    バージョン情報
    """
    return '0.0.6'


class Stopwatch:
    """
    Stopwatch 経過時間を計測するためのクラス。
    Example:
        from src.utils import Stopwatch

        watch = Stopwatch.start_new()
        # 計測する処理
        print(f"{watch.stop():.3f}")
    """

    def __init__(self):
        self._start_time = 0
        self._elapsed = 0

    @property
    def elapsed(self):
        """
        経過時間
        """
        return self._elapsed

    def start(self) -> None:
        """
        計測を開始します。
        """
        self._start_time = time.perf_counter()
        self._elapsed = 0

    @classmethod
    def start_new(cls):
        """
        ストップウォッチを生成し計測を開始します。
        """
        stopwatch = Stopwatch()
        stopwatch.start()
        return stopwatch

    def stop(self):
        """
        計測を終了します。
        """
        end_time = time.perf_counter()
        self._elapsed = end_time - self._start_time
        return self._elapsed

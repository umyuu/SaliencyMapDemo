# -*- coding: utf-8 -*-
"""ユーティリティ"""
import time


def get_package_version() -> str:
    """
    バージョン情報
    """
    return '0.0.7'


class Stopwatch:
    """
    経過時間を計測するためのクラス。
    Example:
        from src.utils import Stopwatch

        watch = Stopwatch.start_new()
        ### 計測する処理
        print(f"{watch.elapsed:.3f}")
    """

    def __init__(self):
        self._start_time: float = 0
        self._elapsed: float = 0
        self._is_running: bool = False

    @property
    def elapsed(self) -> float:
        """
        経過時間を取得します。
        """
        if self._is_running:
            end_time = time.perf_counter()
            self._elapsed = end_time - self._start_time

        return self._elapsed

    def start(self) -> None:
        """
        計測を開始します。
        """
        self._start_time = time.perf_counter()
        self._elapsed = 0
        self._is_running = True

    @classmethod
    def start_new(cls):
        """
        ストップウォッチを生成し計測を開始します。
        """
        stopwatch = Stopwatch()
        stopwatch.start()
        return stopwatch

    def stop(self) -> float:
        """
        計測を終了します。
        """
        if self._is_running:
            end_time = time.perf_counter()
            self._elapsed = end_time - self._start_time
            self._is_running = False
        return self._elapsed

    @property
    def is_running(self) -> bool:
        """
        実行中かどうかを取得します。
        """
        return self._is_running

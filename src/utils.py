# -*- coding: utf-8 -*-
"""ユーティリティ"""
from dataclasses import dataclass
import time


def get_package_version() -> str:
    """
    バージョン情報を取得します。
    """
    return '0.0.8'


@dataclass
class Stopwatch:
    """
    経過時間を計測するためのクラス。
    Example:
        from src.utils import Stopwatch

        watch = Stopwatch.start_new()
        ### 計測する処理
        print(f"{watch.elapsed:.3f}")
    """
    _start_time: float = 0
    _elapsed: float = 0
    _is_running: bool = False

    @property
    def elapsed(self) -> float:
        """
        計測中の経過時間を取得します。

        Returns:
            float: 計測中の経過時間(小数秒)
        """
        if self._is_running:
            self._elapsed = time.perf_counter() - self._start_time

        return self._elapsed

    @property
    def is_running(self) -> bool:
        """
        計測が実行中であるかどうかを取得します
        """
        return self._is_running

    def start(self) -> None:
        """
        計測を開始します。
        """
        self._start_time = time.perf_counter()
        self._elapsed = 0
        self._is_running = True

    @classmethod
    def start_new(cls) -> 'Stopwatch':
        """
        新しいストップウォッチを生成し、計測を開始します。

        Returns:
            Stopwatch: 新しいストップウォッチオブジェクト
        """
        stopwatch = Stopwatch()
        stopwatch.start()
        return stopwatch

    def stop(self) -> float:
        """
        計測を終了し、経過時間を返します。

        Returns:
            float: 計測中の経過時間
        """
        if self._is_running:
            self._elapsed = time.perf_counter() - self._start_time
            self._is_running = False
        return self._elapsed

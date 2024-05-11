# -*- coding: utf-8 -*-
import time

def get_package_version() -> str:
    return '0.0.3'

class Stopwatch:
    """
    Stopwatch 経過時間を計測するためのクラスです。
    Example:
        from utils import Stopwatch
        
        watch = Stopwatch.startNew()
        # 計測する処理
        print(f"{watch.stop():.3f}")
    """

    def __init__(self):
        self._start_time = None
        self._elapsed = 0;

    @property
    def Elapsed(self):
        return self._elapsed

    def start(self) -> None:
        self._start_time = time.perf_counter()
        self._elapsed = 0;

    @classmethod
    def startNew(cls):
        stopwatch = Stopwatch()
        stopwatch.start()
        return stopwatch

    def stop(self):
        end_time = time.perf_counter()
        self._elapsed = end_time - self._start_time
        return self._elapsed

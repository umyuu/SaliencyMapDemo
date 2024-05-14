# -*- coding: utf-8 -*-
"""単体テストモジュール"""
import unittest

import numpy as np
from PIL import Image


class TestGrayscale(unittest.TestCase):
    """
    グレースケールのテスト
    """


def main():
    """
    単体テストのエントリーポイント
    """
    # グラデーションのサイズを定義します
    width = 256
    height = 256

    # numpyを使用してグレースケールのグラデーションを作成します
    gradient = np.linspace(0, 255, width, dtype=np.uint8)

    # 2次元のグラデーションを作成します
    gradient = np.tile(gradient, (height, 1))

    # PIL Imageオブジェクトを作成します
    image = Image.fromarray(gradient, mode='L')

    # 画像を表示します
    image.show()


if __name__ == "__main__":
    #main()
    unittest.main()

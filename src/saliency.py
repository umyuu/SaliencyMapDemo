# -*- coding: utf-8 -*-
"""SaliencyMapを計算する"""
from typing import Any, Tuple, Literal

import numpy as np
import cv2


class SaliencyMap:
    """
    画像から顕著性マップを計算するクラス。

    Example:
        from src.saliency import SaliencyMap

        saliency = SaliencyMap("SpectralResidual")
        success, saliencyMap = saliency.compute(image)
    """
    def __init__(
        self,
        algorithm: Literal["SpectralResidual", "FineGrained"] = "SpectralResidual",
    ):
        """
        SaliencyMapオブジェクトを初期化します。

        Parameters:
            algorithm: 使用する顕著性マップアルゴリズムの種類。
                       有効なアルゴリズムについてはOpenCVのドキュメントを参照してください。
                       https://docs.opencv.org/4.9.0/d8/d65/group__saliency.html

        """
        self.algorithm = algorithm
        # OpenCVのsaliencyを作成します。
        if algorithm == "SpectralResidual":
            self.saliency = cv2.saliency.StaticSaliencySpectralResidual_create()
        else:
            self.saliency = cv2.saliency.StaticSaliencyFineGrained_create()

    def compute(self, image: np.ndarray) -> Tuple[bool, Any]:
        """
        入力画像から顕著性マップを計算します。

        Parameters:
            image: 入力画像

        Returns:
            Tuple[bool, Any]: 顕著性マップの計算結果。
                              bool値がTrueの場合は計算成功、Falseの場合は失敗。
                              顕著性マップのデータ。
        """
        return self.saliency.computeSaliency(image)


def convert_colormap(
    image: np.ndarray,
    saliency_map: np.ndarray,
    colormap_name: Literal["jet", "hot", "turbo"] = "jet"
):
    """
    入力画像と顕著性マップを合成し、指定されたカラーマップを適用します。

    Parameters:
        image: 入力画像
        saliency_map: 顕著性マップ
        colormap_name: カラーマップの種類
            "jet": Jetカラーマップ
            "hot": Hotカラーマップ
            "turbo": Turboカラーマップ

    Returns:
        np.ndarray: 合成された画像 (RGBA形式)
    """
    maps = {"jet": cv2.COLORMAP_JET, "hot": cv2.COLORMAP_HOT, "turbo": cv2.COLORMAP_TURBO}

    # colormap_nameが有効かどうかをチェック
    if colormap_name not in maps:
        raise ValueError(f"Invalid colormap name: {colormap_name}")

    # 顕著性マップをカラーマップに変換
    saliency_map = (saliency_map * 255).astype("uint8")
    saliency_map = cv2.applyColorMap(saliency_map, maps[colormap_name])
    #return saliencyMap
    # 入力画像とカラーマップを重ね合わせ
    overlay = cv2.addWeighted(image, 0.5, saliency_map, 0.5, 0)
    #return overlay
    return cv2.cvtColor(overlay, cv2.COLOR_BGR2RGBA)

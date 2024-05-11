# -*- coding: utf-8 -*-
from typing import Literal

import numpy as np
import cv2


class SaliencyMap:
    """
    SaliencyMap 顕著性マップを計算するクラスです。
    Example:
        from lib.saliency import SaliencyMap
        
        saliency = SaliencyMap("SpectralResidual")
        success, saliencyMap = saliency.computeSaliency(image)
    """
    def __init__(
        self,
        algorithm: Literal["SpectralResidual", "FineGrained"] = "SpectralResidual",
        ):
        self.algorithm = algorithm
        # OpenCVのsaliencyを作成します。
        if algorithm == "SpectralResidual":
            self.saliency = cv2.saliency.StaticSaliencySpectralResidual_create()
        else:
            self.saliency = cv2.saliency.StaticSaliencyFineGrained_create()
        

    def computeSaliency(self, image: np.ndarray):
        """
        入力画像から顕著性マップを作成します。

        Parameters:
            image: 入力画像

        Returns:
           bool:
               true: SaliencyMap computed, false:NG
           np.ndarray: 顕著性マップ               
        """
        # 画像の顕著性を計算します。
        return self.saliency.computeSaliency(image)

def convertColorMap(
    image: np.ndarray,
    saliencyMap: np.ndarray,
    colormap_name: Literal["jet", "hot"] = "jet"):
    """
    顕著性マップをカラーマップに変換後に、入力画像に重ね合わせします。
    
    Parameters:
        image: 入力画像
        saliencyMap: 顕著性マップ
        colormap_name: カラーマップの種類

    Returns:
        np.ndarray: 重ね合わせた画像(RGBA形式)
    """
    #image = (image * 255).astype("uint8")
    #
    #return cv2.applyColorMap(image, cv2.COLORMAP_JET)
    
    
    # 顕著性マップをカラーマップに変換
    saliencyMap = (saliencyMap * 255).astype("uint8")
    if colormap_name == "jet":        
        saliencyMap = cv2.applyColorMap(saliencyMap, cv2.COLORMAP_JET)
    else:
        saliencyMap = cv2.applyColorMap(saliencyMap, cv2.COLORMAP_HOT)
    #return saliencyMap
    # 入力画像とカラーマップを重ね合わせ
    overlay = cv2.addWeighted(image, 0.5, saliencyMap, 0.5, 0)
    #return overlay
    
    return cv2.cvtColor(overlay, cv2.COLOR_BGR2RGBA)

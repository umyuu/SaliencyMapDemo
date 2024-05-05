# -*- coding: utf-8 -*-
"""
    SaliencyMapDemo
"""
import argparse
from datetime import datetime
import sys
from threading import Timer

import cv2
import gradio as gr
import numpy as np

import utils

PROGRAM_NAME = 'SaliencyMapDemo'
__version__ = utils.get_package_version()

def compute_saliency(image: np.ndarray):
    """
        顕著性MAP画像を作成します。
    """
    # OpenCVのsaliencyを作成
    saliency = cv2.saliency.StaticSaliencySpectralResidual_create()
    # 画像の顕著性を計算
    success, saliencyMap = saliency.computeSaliency(image)

    if success:
        # 顕著性マップをカラーマップに変換
        saliencyMap = (saliencyMap * 255).astype("uint8")
        saliencyMap = cv2.applyColorMap(saliencyMap, cv2.COLORMAP_JET)
        
        #overlay = saliencyMap
        # 元の画像とカラーマップを重ね合わせ
        overlay = cv2.addWeighted(image, 0.5, saliencyMap, 0.5, 0)
        
        return overlay
    else:
        return image  # エラーが発生した場合は元の画像を返す

def browser_worker(server_port: int) -> None:
	from webbrowser import open_new_tab
	open_new_tab(f"http://127.0.0.1:{server_port}")

def webbrowser_launch(args: argparse.Namespace) -> None:
	timer = Timer(1, browser_worker, args=[args.server_port])
	timer.start()

def run(args: argparse.Namespace, watch: utils.Stopwatch) -> None:
    """
        アプリの画面を作成し、Gradioサービスを起動します。
    """
    with gr.Blocks(title=f"{PROGRAM_NAME} {__version__}") as demo:
        gr.Markdown(
        """
        # Saliency Map demo.
        1. inputタブで画像を選択します。
        2. Submitボタンを押します。※外部送信していません。ローカルで完結しています。
        3. 結果がoverlayタブに表示されます。
        """)

        submit_button = gr.Button("submit")
        
        with gr.Row():
            with gr.Tab("input"):
                image_input = gr.Image()
            with gr.Tab("overlay"):
                image_overlay = gr.Image(interactive=False)

        
        submit_button.click(compute_saliency, inputs=image_input, outputs=image_overlay)

        gr.Markdown(
        f"""
        Python {sys.version}  
        App {__version__}  
        """)
        
        demo.queue(default_concurrency_limit=5)
        
        webbrowser_launch(args)
        
        print(f"{datetime.now()}:アプリ起動完了({watch.stop():.3f}s)")
        
        demo.launch(max_file_size=args.max_file_size, server_port=args.server_port)

# -*- coding: utf-8 -*-
"""
    SaliencyMapDemo
"""
import argparse
import cv2
import gradio as gr
import numpy as np
import sys

PROGRAM_NAME = 'SaliencyMapDemo'
__version__ = '0.0.1'

def compute_saliency(image: np.ndarray):
    # OpenCVのsaliencyを作成
    saliency = cv2.saliency.StaticSaliencySpectralResidual_create()
    # 画像の顕著性を計算
    success, saliencyMap = saliency.computeSaliency(image)

    if success:
        # 顕著性マップをカラーマップに変換
        saliencyMap = (saliencyMap * 255).astype("uint8")
        saliencyMap = cv2.applyColorMap(saliencyMap, cv2.COLORMAP_JET)
        # 元の画像とカラーマップを重ね合わせ
        overlay = cv2.addWeighted(image, 0.5, saliencyMap, 0.5, 0)
        return overlay
    else:
        return image  # エラーが発生した場合は元の画像を返す

def main(args):    
    """
        Entry Point
    """
    with gr.Blocks() as demo:
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
                image_overlay = gr.Image()

        
        submit_button.click(compute_saliency, inputs=image_input, outputs=image_overlay)
        sys.version
        gr.Markdown(
        f"""
        Python {sys.version}  
        App {__version__}  
        """)
        demo.queue(default_concurrency_limit=5).launch(max_file_size=args.max_file_size, server_port=args.server_port)

if __name__ == "__main__":
    """
        コマンドライン引数の解析
    """
    parser = argparse.ArgumentParser(prog=PROGRAM_NAME, description="SaliencyMapDemo")
    parser.add_argument('--server_port', type=int, default=9999, help="Gradio server port")
    parser.add_argument('--max_file_size', type=int, default=20 * gr.FileSize.MB, help="Gradio max file size")
    parser.add_argument('--version', action='version', version='%(prog)s {0}'.format(__version__))

    main(parser.parse_args())


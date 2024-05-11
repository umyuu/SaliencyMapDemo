# -*- coding: utf-8 -*-
"""
    SaliencyMapDemo
"""
import argparse
from datetime import datetime
import sys

import gradio as gr
import numpy as np

import utils
from saliency import SaliencyMap, convertColorMap
from reporter import get_current_reporter
        
PROGRAM_NAME = 'SaliencyMapDemo'
__version__ = utils.get_package_version()
log = get_current_reporter()

def jetTab_Selected(image: np.ndarray):
    #print(f"{datetime.now()}#jet")
    saliency = SaliencyMap("SpectralResidual")
    success, saliencyMap = saliency.computeSaliency(image)
    retval = convertColorMap(image, saliencyMap, "jet")
    #print(f"{datetime.now()}#jet")
    
    return retval
    
def hotTab_Selected(image: np.ndarray):
    #print(f"{datetime.now()}#hot")
    saliency = SaliencyMap("SpectralResidual")
    success, saliencyMap = saliency.computeSaliency(image)
    retval = convertColorMap(image, saliencyMap, "hot")
    #print(f"{datetime.now()}#hot")
    
    return retval

def submit_Clicked(image: np.ndarray, algorithm: str):
    """
    入力画像を元に顕著マップを計算します。

    Parameters:
        image: 入力画像
        str: 顕著性マップのアルゴリズム
    Returns:
        np.ndarray: JET画像
        np.ndarray: HOT画像
    """
    log.info(f"#submit_Clicked")
    watch = utils.Stopwatch.startNew()
    
    saliency = SaliencyMap(algorithm)
    success, saliencyMap = saliency.computeSaliency(image)
    log.info(f"#SaliencyMap computeSaliency()")

    if not success:
        return image, image # エラーが発生した場合は入力画像を返します。

    log.info(f"#jet")        
    jet = convertColorMap(image, saliencyMap, "jet")
    #jet = None
    log.info(f"#hot")
    hot = convertColorMap(image, saliencyMap, "hot")
    
    saliency = None
    log.info(f"#submit_Clicked End{watch.stop():.3f}")
    return jet, hot

def run(args: argparse.Namespace, watch: utils.Stopwatch) -> None:
    """
    アプリの画面を作成し、Gradioサービスを起動します。

    Parameters:
        args: コマンドライン引数
        watch: 起動したスタート時間
    """
    # analytics_enabled=False
    # https://github.com/gradio-app/gradio/issues/4226
    with gr.Blocks(analytics_enabled=False, \
        title=f"{PROGRAM_NAME} {__version__}", \
        head="""
        <meta name="format-detection" content="telephone=no">
        <meta name="robots" content="noindex, nofollow, noarchive">
        <meta name="referrer" content="no-referrer" />
        """) as demo:
    	
        gr.Markdown(
        """
        # Saliency Map demo.
        """)
        with gr.Accordion("取り扱い説明書", open=False):
            gr.Markdown(
            """
            1. inputタブで画像を選択します。
            2. Submitボタンを押します。
               ※画像は外部送信していません。ローカルで処理が完結します。
            3. 結果は、JETタブとHOTタブに表示します。  
            """)

        algorithmType = gr.Radio(["SpectralResidual", "FineGrained"], label="Saliency", value="SpectralResidual", interactive=True)

        submit_button = gr.Button("submit")

        with gr.Row():
            with gr.Tab("input", id="input"):

                image_input = gr.Image(sources = ["upload", "clipboard"], interactive=True)
            with gr.Tab("overlay(JET)"):
                image_overlay_jet = gr.Image(interactive=False)
                #tab_jet.select(jetTab_Selected, inputs=[image_input], outputs=image_overlay_jet)
            with gr.Tab("overlay(HOT)"):
                image_overlay_hot = gr.Image(interactive=False)
                #tab_hot.select(hotTab_Selected, inputs=[image_input], outputs=image_overlay_hot, api_name=False)
        
        submit_button.click(submit_Clicked, inputs=[image_input, algorithmType], outputs=[image_overlay_jet, image_overlay_hot])

        gr.Markdown(
        f"""
        Python {sys.version}  
        App {__version__}  
        """)
        
        demo.queue(default_concurrency_limit=5)
        
        log.info(f"#アプリ起動完了({watch.stop():.3f}s)")
        
        # https://www.gradio.app/docs/gradio/blocks#blocks-launch
        demo.launch(
            max_file_size=args.max_file_size,
            server_port=args.server_port,
            inbrowser=True,
            share=False,
        )

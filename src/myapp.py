# -*- coding: utf-8 -*-
"""myapp Widget"""
from typing import Literal

import argparse
#from datetime import datetime
import sys

import gradio as gr
import numpy as np

from src.utils import Stopwatch, get_package_version
from src.saliency import SaliencyMap, convert_colormap
from src.reporter import get_current_reporter

PROGRAM_NAME = 'SaliencyMapDemo'
__version__ = get_package_version()
log = get_current_reporter()
log.info("#アプリ起動中")
watch = Stopwatch.start_new()


def jet_tab_selected(image: np.ndarray):
    """
    JETタブを選択時
    """
    #print(f"{datetime.now()}#jet")
    saliency = SaliencyMap("SpectralResidual")
    success, saliency_map = saliency.compute(image)
    if not success:
        return image  # エラーが発生した場合は入力画像を返します。
    retval = convert_colormap(image, saliency_map, "jet")
    #print(f"{datetime.now()}#jet")
    return retval


def hot_tab_selected(image: np.ndarray):
    """
    HOTタブを選択時
    """
    #print(f"{datetime.now()}#hot")
    saliency = SaliencyMap("SpectralResidual")
    success, saliency_map = saliency.compute(image)
    if not success:
        return image  # エラーが発生した場合は入力画像を返します。
    retval = convert_colormap(image, saliency_map, "turbo")
    #print(f"{datetime.now()}#hot")
    return retval


def submit_clicked(image: np.ndarray, algorithm: Literal["SpectralResidual", "FineGrained"]):
    """
    入力画像を元に顕著マップを計算します。

    Parameters:
        image: 入力画像
        str: 顕著性マップのアルゴリズム
    Returns:
        np.ndarray: JET画像
        np.ndarray: HOT画像
    """
    #log.info(f"#submit_Clicked")
    #watch = utils.Stopwatch.startNew()
    #
    saliency = SaliencyMap(algorithm)
    success, saliency_map = saliency.compute(image)
    # log.info(f"#SaliencyMap compute()")

    if not success:
        return image, image  # エラーが発生した場合は入力画像を返します。

    # log.info(f"#jet")
    jet = convert_colormap(image, saliency_map, "jet")
    # jet = None
    # log.info(f"#hot")
    hot = convert_colormap(image, saliency_map, "hot")
    saliency = None
    #log.info(f"#submit_Clicked End{watch.stop():.3f}")
    return jet, hot


def run_app(args: argparse.Namespace) -> None:
    """
    アプリの画面を作成し、Gradioサービスを起動します。

    Parameters:
        args: コマンドライン引数
        watch: 起動したスタート時間
    """
    # analytics_enabled=False
    # https://github.com/gradio-app/gradio/issues/4226
    with gr.Blocks(
        analytics_enabled=False,
        title=f"{PROGRAM_NAME} {__version__}",
        head="""
        <meta name="format-detection" content="telephone=no">
        <meta name="robots" content="noindex, nofollow, noarchive">
        <meta name="referrer" content="no-referrer" />
        """
    ) as demo:

        gr.Markdown("""
            # Saliency Map demo.
            """)
        with gr.Accordion("取り扱い説明書", open=False):
            gr.Markdown("""
                1. inputタブで画像を選択します。
                2. Submitボタンを押します。
                3. 結果は、JETタブとHOTタブに表示します。  
            """)
        algorithm_type = gr.Radio(
            ["SpectralResidual", "FineGrained"],
            label="Saliency",
            value="SpectralResidual",
            interactive=True
        )

        submit_button = gr.Button("submit", variant="primary")

        with gr.Row():
            with gr.Tab("input", id="input"):
                image_input = gr.Image(sources=["upload", "clipboard"],
                                       interactive=True)
            with gr.Tab("overlay(JET)"):
                image_overlay_jet = gr.Image(interactive=False)
                # tab_jet.select(jet_tab_selected,
                # inputs=[image_input],
                # outputs=image_overlay_jet)
            with gr.Tab("overlay(HOT)"):
                image_overlay_hot = gr.Image(interactive=False)
                # tab_hot.select(hot_tab_selected,
                # inputs=[image_input],
                # outputs=image_overlay_hot, api_name=False)
        #
        submit_button.click(
            submit_clicked,
            inputs=[image_input, algorithm_type],
            outputs=[image_overlay_jet,
                     image_overlay_hot]
        )

        gr.Markdown(f"""
            Python {sys.version}  
            App {__version__}  
        """)

        demo.queue(default_concurrency_limit=5)

        log.info(f"#アプリ起動完了({watch.stop():.3f}s)")
        # https://www.gradio.app/docs/gradio/blocks#blocks-launch
        demo.launch(
            inbrowser=args.inbrowser,
            share=args.share,
            server_port=args.server_port,
            max_file_size=args.max_file_size,
        )

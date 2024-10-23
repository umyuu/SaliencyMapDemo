# -*- coding: utf-8 -*-
"""
    SaliencyMapDemo
"""

#from datetime import datetime
import sys
from typing import Literal

import gradio as gr
import numpy as np

from src import PROGRAM_NAME, get_package_version
from src.args_parser import parse_args
from src.reporter import log
from src.saliency import SaliencyMap, convert_colormap
from src.utils import Stopwatch

__version__ = get_package_version()
log.info("#アプリ起動中")
watch = Stopwatch.start_new()


def jet_tab_selected(image: np.ndarray):
    """
    JETタブを選択時
    """
    sw = Stopwatch.start_new()
    log.info(f"#jet_tab_selected({sw.elapsed:.3f}s)")
    saliency = SaliencyMap("SpectralResidual")
    success, saliency_map = saliency.compute(image)
    if not success:
        return image  # エラーが発生した場合は入力画像を返します。
    retval = convert_colormap(image, saliency_map, "jet")
    log.info(f"#jet_tab_selected({sw.elapsed:.3f}s)")
    return retval


def hot_tab_selected(image: np.ndarray):
    """
    HOTタブを選択時
    """
    sw = Stopwatch.start_new()
    log.info(f"#hot_tab_selected({sw.elapsed:.3f}s)")
    saliency = SaliencyMap("SpectralResidual")
    success, saliency_map = saliency.compute(image)
    if not success:
        return image  # エラーが発生した場合は入力画像を返します。
    retval = convert_colormap(image, saliency_map, "turbo")
    log.info(f"#hot_tab_selected({sw.elapsed:.3f}s)")
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
    sw = Stopwatch.start_new()
    log.info(f"#submit_clicked({sw.elapsed:.3f}s)")
    #
    saliency = SaliencyMap(algorithm)
    log.debug(f"#SaliencyMap({sw.elapsed:.3f}s)")
    success, saliency_map = saliency.compute(image)
    log.debug(f"#compute({sw.elapsed:.3f}s)")

    if not success:
        return image, image  # エラーが発生した場合は入力画像を返します。

    log.debug(f"#jet({sw.elapsed:.3f}s)")
    jet = convert_colormap(image, saliency_map, "jet")
    # jet = None
    log.debug(f"#hot({sw.elapsed:.3f}s)")
    hot = convert_colormap(image, saliency_map, "hot")
    saliency = None
    log.info(f"#submit_clicked({sw.elapsed:.3f}s)")
    return jet, hot


def gallery_selected(_, evt: gr.SelectData):
    """
    ギャラリーの画像が選択されたときに呼び出されるコールバック関数。

    Parameters:
        _ (Unused): 使用されない引数。
        evt (gr.SelectData): Gradioのギャラリー選択イベントデータ。
    Returns:
        str: 選択されたギャラリー画像のパス。
    """
    image_path = evt.value['image']['path']

    return image_path


args = parse_args()
"""
アプリの画面を作成し、Gradioサービスを起動します。
    ホットリロード対応として、topレベルのインデントに。
    https://www.gradio.app/guides/developing-faster-with-reload-mode
"""
with gr.Blocks(
    title=f"{PROGRAM_NAME} {get_package_version()}",
    head="""
    <meta name="format-detection" content="telephone=no">
    <meta name="robots" content="noindex, nofollow, noarchive">
    <meta name="referrer" content="no-referrer" />
    """
) as demo:
    gr.Markdown("""
        # Saliency Map demo.  
          画像における注目すべき領域を可視化する「顕著性マップ」を表示するデモアプリです。  
        """)

    with gr.Accordion("取り扱い説明書", open=False):
        gr.Markdown("""
            ## 顕著性マップとは  
            顕著性マップとは、画像内の注目すべき領域を視覚化する手法です。この手法は、人間の視覚システムが重要な情報に焦点を当てる方法を模倣しています。各ピクセルには、その注目度合いを表す値が割り当てられ、それに基づいて注目すべき領域が強調されます。  
            ## 操作説明  
            顕著性マップデモを使用する手順は以下の通りです：  
            1. 画像の選択: inputタブで調査したい画像を選択します。下部の📋クリップボードアイコン（コピー&ペーストアイコン）よりクリップボートから入力することも出来ます。  
            2. マップの生成: Submitボタンをクリックすると、選択した画像が処理され、重ね合わされた顕著性マップが生成されます。  
            3. 結果の確認: 生成された顕著性マップは、JETタブとHOTタブに表示されます。  
            ### 活用アイデア🎨  
            このデモは、創作活動の際に注目するポイントを視覚化するために役立ちます。視覚化された結果を基に、どの部分に加筆が必要かを判断することができます。  
            たとえば、顔の目に注目ポイントが少ない場合、その部分を重点的に加筆することで、作品全体の魅力を高めることができるかもしれません。  
            ご利用いただき、ありがとうございます。  
        """)
    with gr.Accordion("Saliency Map User Guide", open=False):
        gr.Markdown("""
            ## Learn about saliency maps:  
            A saliency map visually highlights important areas in an image, mimicking how humans focus on key information.  
                     Each pixel is assigned a value representing attention level, highlighting regions of interest.  
            ### Try the demo:  
            To use the saliency map demo, follow two steps  
            1. Upload an image or paste it from the clipboard.  
            2. Click "Submit" to generate and view the saliency map on separate tabs.  
            ### Application Ideas🎨.  
            Useful for creative projects to identify points of interest and enhance appeal.  
                     For instance, if eyes are focal points, focus enhancements there.  
            Thank you for your interest!  
        """)

    submit_button = gr.Button("submit", variant="primary")
    with gr.Tab("input", elem_id="input_tab"):
        image_input = gr.Image(label="input", show_label=True, sources=["upload", "clipboard"])
    with gr.Tab("overlay(JET)", elem_id="jet_tab"):
        image_overlay_jet = gr.Image(label="jet", show_label=True, interactive=False)
    with gr.Tab("overlay(HOT)", elem_id="hot_tab"):
        image_overlay_hot = gr.Image(label="hot", show_label=True, interactive=False)

    with gr.Accordion("Advanced options", open=False):
        algorithm_type = gr.Radio(
            ["SpectralResidual", "FineGrained"],
            label="Saliency",
            value="SpectralResidual",
            interactive=True
        )

    with gr.Accordion("Examples", open=False):
        gr.Markdown("""
            ### 画像のライセンス表示  
            画像のライセンスはすべてCC0(パブリックドメイン)です。
        """)
        gallery = gr.Gallery(type="filepath",
                             value=["assets/black_256x256.webp",
                                    "assets/grayscale_256x256.webp",
                                    "assets/DSC_0108.webp", 
                                    "assets/DSC_0297.webp"], 
                             label="Sample Gallery",
                             interactive=False,
                             #height=156,
                             columns=5,
                             allow_preview=False,
                             selected_index=0,
                             preview=False,
                             show_download_button=False,
                             show_share_button=False
                             )
    # ギャラリー内の画像を選択時
    gallery.select(gallery_selected,
                   inputs=[gallery],
                   outputs=[image_input],
                   show_api=False
                   )
    submit_button.click(
        submit_clicked,
        inputs=[image_input, algorithm_type],
        outputs=[image_overlay_jet, image_overlay_hot]
    )
    gr.Markdown(f"""
        Python {sys.version}  
        App {get_package_version()}  
    """)

    demo.queue(default_concurrency_limit=5)

    log.info(f"#アプリ起動完了({watch.elapsed:.3f}s)アプリを終了するにはCtrl+Cキーを入力してください。")
    log.debug("reload")


if __name__ == "__main__":
    # アプリを起動します。
    # https://www.gradio.app/docs/gradio/blocks#blocks-launch
    demo.launch(
        inbrowser=args.inbrowser,
        share=args.share,
        server_port=args.server_port,
        max_file_size=args.max_file_size,
    )

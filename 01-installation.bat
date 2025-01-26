REM uvのキャッシュパスの変更（SSD最適化）
REM 通常のキャッシュ場所をSSD上の指定したパス（K:\uv_cache）にリンクすることで、
REM キャッシュの読み書き速度を最適化します。リンクが必要な場合のみ有効です。
REM mklink /d %LOCALAPPDATA%\uv\cache K:\uv_cache

REM pip経由でuvをインストール
pip install uv

REM uvの依存関係を同期
REM `uv sync`を使って、プロジェクトの依存関係を`pyproject.toml`および`uv lock`ファイルに基づいてインストールまたは更新します。
REM これにより、環境が同期され、必要なライブラリがインストールされます。
uv sync --reinstall

TIMEOUT /T 10

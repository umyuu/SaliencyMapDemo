REM uv�̃L���b�V���p�X�̕ύX�iSSD�œK���j
REM �ʏ�̃L���b�V���ꏊ��SSD��̎w�肵���p�X�iK:\uv_cache�j�Ƀ����N���邱�ƂŁA
REM �L���b�V���̓ǂݏ������x���œK�����܂��B�����N���K�v�ȏꍇ�̂ݗL���ł��B
REM mklink /d %LOCALAPPDATA%\uv\cache K:\uv_cache

REM pip�o�R��uv���C���X�g�[��
pip install uv

REM uv�̈ˑ��֌W�𓯊�
REM `uv sync`���g���āA�v���W�F�N�g�̈ˑ��֌W��`pyproject.toml`�����`uv lock`�t�@�C���Ɋ�Â��ăC���X�g�[���܂��͍X�V���܂��B
REM ����ɂ��A������������A�K�v�ȃ��C�u�������C���X�g�[������܂��B
uv sync --reinstall

TIMEOUT /T 10

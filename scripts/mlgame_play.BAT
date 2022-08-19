set PYTHON_PATH="python.exe所在目錄路徑"
set PATH=%PYTHON_PATH%;%PATH%
cd ..
python -m mlgame -f 30 -i ./ai_clients/arkanoid/RL_Like/ml_play.py ./games/arkanoid --difficulty EASY --level 3
PAUSE

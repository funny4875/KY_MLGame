set PYTHON_PATH="C:\Users\ky\AppData\Local\Programs\Python\Python39\"
set PIP_PATH="C:\Users\ky\AppData\Local\Programs\Python\Python39\Scripts"
set PATH=%PYTHON_PATH%;%PIP_PATH%
python --version
pip --version
cd ..
python -m mlgame -f 30 -i ./ai_clients/arkanoid/RL_Like/ml_play.py ./games/arkanoid --difficulty EASY --level 3
PAUSE
#python mlgame.py -i ml_play.py -f 60 arkanoid --difficulty EASY --level 18
#echo %PATH%
#set arkanoid="C:\Users\ky\OneDrive\Desktop\MLGame\games\arkanoid"
#set ml_play="C:\Users\ky\OneDrive\Desktop\MLGame\games\arkanoid\ml\ml_play.py"

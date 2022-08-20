set pythonPath="python.exe所在目錄路徑"
set scriptsPath="pip.exe所在目錄路徑"
set path=%scriptsPath%;%path%
set path=%pythonPath%;%path%
pip install scikit-learn
pip install mlgame
pause
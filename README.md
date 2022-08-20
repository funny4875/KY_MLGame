# MLGameDemo
## MLGame簡化版 
### 本範例只提供 windows 版本
#### games資料夾中只下載 打磚塊(arkanoid)、打乒乓(pingpong) 兩種遊戲
#### 若需要其它遊戲 ex:賽車　請至PAIA官方github下載
#### <a ref=https://github.com/PAIA-Playful-AI-Arena/Paia-Desktop#downloads> https://github.com/PAIA-Playful-AI-Arena/Paia-Desktop#downloads </a>
### 本專案提供一種由失敗經驗中做機器學習去
### 回歸預測球的落點x座標的script，原始碼位於
<code> ai_clients\arkanoid\RL_Like\ml_play.py </code> 
#### 可直接執行scrtips資料夾中的
#### mlgame_play.BAT 觀看效果

#### <a ref=https://youtu.be/-bsTl-3QoRg>操作示範影片</a>

### 
### ● Step1.請先安裝 python3.9 
### ● Step2.並於python3.9環境中安裝 sklearn 及 mlgame
####       <code> pip install scikit-learn </code>
####       <code> pip install mlgame </code>
### 
### ● Step3.修改 scripts\mlgame_play.BAT 的變數 『pythonPath]』 為『python.exe所在路徑(python3.9)』
### ● Step4.執行 mlgame_play.BAT
####        修改 level 參數，多玩幾關後，下列ai模型將越來越強
####        <code> ai_clients\arkanoid\RL_Like\model.pickle</code> 
### 再次強調本範例只適用 windows 版本

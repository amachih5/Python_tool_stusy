"""
#math（数学系）
import math 
print("円周率: ", math.pi)
print("√2= :", math.sqrt(2))
print("5! = : ", math.factorial(5))
"""

"""
#datetime（今日の日付）
from datetime import datetime
today = datetime.now()
print("今日は: ", today.strftime(".%Y年%m月%d日 %H時:%M分"))
print("LoStationリリースまであと", (datetime(2026, 7, 30) - today).days, "日")
"""

"""
#ramdom（Mbappéのゴールシミュレーション）
import random
print("今日のMbappéのゴール数: ", random.randint(0, 5))
"""

"""
#requests（駅のAPI取る時に役立つ）
import requests
# 例：現在地から最寄り駅取得（無料API）
url = "https://express.heartrails.com/api/json?method=getStations&x=139.767125&y=35.681236"

response = requests.get(url)
data = response.json()

print("東京駅周辺の駅: ", [s["name"]for s in data["response"]["station"][:5]])
"""

#pandas(お父さんのExcel自動処理）← これで自営業手伝える！！)
import pandas as pd

# ダミーの自営業売上データ
df = pd.DataFrame({
  "日付": ["2025-12-01", "2025-12-02", "2025-12-03"],
  "商品": ["飛騨牛", "けいちゃん", "五平餅"],
  "売上": [5000, 3000, 2000],
})

print("お父さんの売上")
print(df)
print("合計売上: ",df["売上"].sum(), "円！")
df.to_excel("お父さんの売上_202512.xlsx", index=False)
print("保存完了！")

"""
rma = {
  "Mbappé": 9,
  "Vinicius": 7,
  "Rodrygo": 11,
  "Bellingham": 5,
  "Courtois": 1
}
print(rma["Mbappé"])
print(rma.get("Mbappé"))

#追加、変更、削除
rma["Modric"] = 10
rma["Mbappé"] = 7
del rma["Modric"]
print(rma)
"""

"""
#自分のデータ辞書
hayato = {"age": 23, "job": "セブンバイト", "team": "RMA", "hero": "Mbappé"}
print(f"{hayato['hero']}のユニフォームをもっている{hayato['age']}歳のはやと")
"""

"""
#paiza対策
n = int(input()) #選手何人？
players = {}
for _ in range(n):
  name, number = input().split() #Mbappé 9
  players[name] = int(input())   #辞書に追加
find = input() #調べる選手名を入力
print(players.get(find, "いないよ")) #いなかったらメッセージ
"""

rma_goals = {
  "Mbappé": 50, 
  "Vinicius": 25,  #今季ゴール数（仮）
  "Bellingham": 20, 
  "Rodrygo": 10,
  "Kroos": 7
}

#values() 値だけ全部とる
print(sum(rma_goals.values()))


#items() キーと値のペアを全部とる
for name, goals in rma_goals.items():
  print(f"{name}: 今季{goals}ゴール！")


#in キーがいるかチェック（超便利）
if "Mbappé" in rma_goals:
  print("エースいる！")

#sorted 並び替え（ゴール数が多い順）
sorted_players = sorted(rma_goals.items(), key=lambda x: x[1], reverse=True)
#x[1]が値（ゴール数）だからこれで降順
print(sorted_players)

#内包表記で新しい辞書作る（神テク）
#20ゴール以上の選手だけ抜き出して「エース辞書」を作る
aces = {name: goals for name, goals in rma_goals.items() if goals >= 20}
print(aces)

"""
覚えとけポイント

{}で作る
dict["キー"]で取る（キーないとエラー）
.get("キー", "デフォルト")が神（ない時も安心）
LoStationで「駅名 → 緯度経度」とか絶対使う！！
"""

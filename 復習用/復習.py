"""
#標準入力
name = "はやと"
age = 23
print(f"{name}さんは{age}歳です")
"""
"""
#演算と数値
wage = 1140 * 8.5
print(f"今日の給料: {int(wage)}円！")
"""

"""
#岐阜で食べたものリスト
gifu_food = ["飛騨牛", "けいちゃん", "五平餅"]
gifu_food.append("味噌カツ")
print(gifu_food)
"""

"""
#リスト内包表記（昨日やったやつで遊ぶ）
tolls = [x * 500 for x in range(1, 11)]
print("高速料金リスト: ", tolls)
print("合計: ", sum(tolls), "円、痛いな〜")
"""

"""
#ブール型
is_madrid_fan = True
is_mbappe_fan = True
print(is_madrid_fan and is_mbappe_fan)
print(is_madrid_fan and is_mbappe_fan)
"""

#条件分岐
goals = 52
if goals >= 50:
  print("バケモノ！！")
elif goals >= 30:
  print("エース級！！")
else:
  print("もっと頑張れ！")

"""
#while文
energy = 10
while energy > 0:
  print(f"残りエネルギー: {energy}...もう寝たい")
  energy -= 3
print("寝落ち...おやすみ")
"""
#for文 + range
print("12月の予定")
for day in range(1, 6):
  if day == 1:
    print(f"12/{day:2d}今日！ブール~ for文復習")
  elif day == 5:
    print(f"12/{day:2d}プロトタイプ開始")
  else:
    print(f"12/{day:2d}復習&ミニアプリ")

#for文 + リスト　お土産リスト
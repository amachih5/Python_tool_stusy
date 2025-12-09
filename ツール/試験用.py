"""
#気分を辞書に貯める
kibun_dict= {}
for _ in range(7):
  day = input("曜日を入力: ")
  kibun_day = input("曜日ごとの気分を入力: ")

  kibun_dict[day] = kibun_day
print("完成系", kibun_dict)

"""
"""
#給料計算ツール
class Salary:
  def __init__(self, name, hourly, hours):
    self.name = name
    self.hourly = hourly
    self.hours = hours


  def calc_month_salary(self, midnight=0):
    basic_salary = self.hourly * self.hours
    midnight_bonus = self.hourly * midnight * 1.25
    total_salary= basic_salary + midnight_bonus
    return f"{self.name}さんは時給{self.hourly}円で{self.hours}時間働いたので、今月の給料は{total_salary}円です。"

hayato = Salary("はやと", 1140, 40)
print(hayato.calc_month_salary())
"""

"""
#最新ニュースを取得してみる
import requests

headers = {
  'API_KEY': 'ef85020308774fb4bbf792016d3ea1c5'
  }

url = 'https://newsai/org/v2/everything'
paras = {
  'q': '鉄道',
  'sortBy': 'publishedAt',
  'pageSize': 10
}

response = requests.get(url, headers=headers, params=paras)

print(response)
"""

"""
#テストの結果を辞書に起こしてみる
object_num = int(input("何教科受けましたか？: "))
name = input("名前を入力してください: ")

object_dict ={}
for _ in range(object_num):
  object_name = input("教科名を入力: ")
  point = int(input("点数を入力: "))
  object_dict[object_name] = point

total = sum(object_dict.values())
average = total / object_num

print(f"{name}さんの合計点: {sum(object_dict.values())}点！、平均{average}点！")
"""

"""
#ここからご褒美ツールに応用してみる
gohoubi =["Switch", "旅行券", "お菓子"]

name = input("名前を入力してください: ")
test_num = int(input("教科数を入力: "))

test_d = {}
for _ in range(test_num):
  name =  input("教科名: ")
  point = int(input("点数: "))
  test_d[name] = point

total = sum(test_d.values())
average = total / test_num 

if average >= 90:
  print(f"{gohoubi[0]}をプレゼント！")
elif average >= 75:
  print(f"{gohoubi[1]}をプレゼント！")
elif average >= 60:
  print(f"{gohoubi[2]}をプレゼント！")
else:
  print("もっと頑張りましょう")
"""

"""
#1年間の定期試験管理ツール
def exam_tool():
  gohoubi = ["switch", "旅行券", "お菓子", "頑張ったね賞"]

  name = input("名前を入力: ")
  print(f"{name}さんの1年間の成績を入力します")

  yearly_scores = {}
  for exam_num in range(1, 5):
    print(f"\n--- 第{exam_num}回 定期試験 ---")
    test_num = int(input("教科数を入力: "))
    test_d = {}
    for _ in range(test_num):
      subject = input("教科名: ")
      point = int(input("点数: " ))
      test_d[subject] = point
    
    total = sum(test_d.values())
    average = total / test_num

    yearly_scores[f"第{exam_num}回"] = {
      "結果": test_d,
      "合計点": total,
      "平均点": average
    }

    print(f"第{exam_num}回平均: {average:.1f}点")

  all_averages = [data["平均点"]for data in yearly_scores.values()]
  yearly_average = sum(all_averages) / 4
  
  print(f"\n {name}さんの1年間の平均点: {yearly_average:.1f}点！")

  if yearly_average >= 90:
    print(f"{gohoubi[0]}をプレゼント！")
  elif yearly_average >= 80:
    print(f"{gohoubi[1]}をプレゼント！")
  elif yearly_average >= 70:
    print(f"{gohoubi[2]}をプレゼント！")
  else:
    print(f"{gohoubi[3]}をプレゼント！次も頑張ろう！")

exam_tool()
"""
"""
import math 
M = 9.0
log_E = 1.5 * M + 4.8
E = 10 ** log_E
tnt_per_ton = 4.184e9
tnt_megatons = (E / tnt_per_ton) / 1e6


tsar_bomba_mt = 50
hiroshima_kt = 15
hiroshima_mt = hiroshima_kt / 1000

tsar_equiv = tnt_megatons / tsar_bomba_mt
hiroshima_equiv = tnt_megatons / hiroshima_mt

print(f"M9.0の地震: 約{tnt_megatons:.0f}メガトンTNT")
print(f"ツァーリボンバ約{tsar_equiv:.1f}個分")
print(f"広島型原爆約{hiroshima_equiv:.1f}個分")
"""

"""
#年間売上計算ツール
def sales_tool():
  #売上高＝ 販売単価*販売数量
  uriagemono = input("売ったものを入力: ")
  total_sales_d = {}
  for _ in range(12):
    sale_month = input("販売月を入力: ")
    sale_one = int(input("販売単価を入力: "))
    sale_volume  = int(input("販売した量を入力: "))
    total_sales = sale_one * sale_volume
    total_sales_d[sale_month] = total_sales
  print(f"{uriagemono}の月ごとの売上: {total_sales_d}, 年間売上: {sum(total_sales_d.values())}円")
sales_tool()
"""

#じゃんけん判定
import random

def janken_judge():
  while True:
    try:
        player_hands = input("じゃんけんの手をいれてね: ")
        if player_hands not in ["グー", "チョキ", "パー"]:
          print("正しい手を入れてね！: ")
    except ValueError:
      print("入力ミスかも! もう一回入れてみてね: ")
      
    
    cp_hands = random.choice(["グー", "チョキ", "パー"])
    print(f"プレイヤーの手は{player_hands}, コンピューターの手は{cp_hands}です。判定は...")
    if (player_hands == "パー" and cp_hands == "グー") or (player_hands == "グー" and cp_hands == "チョキ") or (player_hands == "チョキ" and cp_hands == "パー"):
      print("勝ち！ やるやん")
      c = input("続けますか？ y/n: ")
      if c == "y":
        continue
      else:
        print("またね")
        break
    elif player_hands == cp_hands:
      print("引き分け！")
      c1 = input("もう一回やる？: y/n: ")
      if c1 == "y":
        continue
      else:
        print("またね")
        break
    
    else:
      print("CPの勝ち!なんで負けたか明日までに考えておいてださい!")
      c2 = input("もう一回やる？ y/n: ")
      if c2 == "y":
        print("やるやん！もう一回！")
        continue
      else:
        print("また今度も僕が勝ちますよ！")
        break
    
janken_judge()





  


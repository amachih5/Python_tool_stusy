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
"""
"""
import pandas as pd
def sales_auto_tool():
  sales_d = {}
  n = int(input("商品の個数を入力: "))
  for _ in range(n):
    item = input("商品名: ")
    price = int(input("売上額: "))
    sales_d[item] = price

  total = sum(sales_d.values())
  average = total / n if n > 0 else 0
  print(f"合計売上: {total}円, 平均: {average:.1f}円")

  df = pd.DataFrame(list(sales_d.item()), columns= ["商品", "売上"])
  df.to_excel("Excel保存完了!")
sales_auto_tool()
"""

"""
def calc_shopping():
  shopping_volume = int(input("買い物する個数を入力: "))
  shopping_d = {}
  for _ in range(shopping_volume):
    shopping_thing = input("買うものを入力: ")
    shopping_value = int(input("値段を入力: "))
    shopping_d[shopping_thing] = shopping_value
  return f"買い物をするもの: {shopping_d}、合計: {sum(shopping_d.values())}円"
  
shopping = calc_shopping()
print(shopping)
"""

"""
#在庫管理ツール
zaiko_d ={}
def zaiko_manage():
  n = int(input("在庫数を確認: "))
  for _ in range(n):
    goods = input("商品名を入力: ")
    volome = int(input("在庫数を入力: "))
    zaiko_d[goods] = volome
  return f"在庫一覧: {zaiko_d}"

#ふやす
def zaiko_append():
  zaiko_append_question = input("追加しますか？: y/n: ")
  if zaiko_append_question == "y":
    goods = input("追加する商品を入力: ")
    volome = int(input("追加する個数を入力: "))
    zaiko_d[goods] = volome
    return f"在庫が追加されました! 商品: {zaiko_d}"
  
  else:
    print("追加をキャンセルしました。")
    
#減らす 
def zaiko_delete(): 
  zaiko_delete_question = input("在庫を削除しますか？: y/n: ")
  if zaiko_delete_question == "y":
    goods = input("削除する商品を入力: ")
    del zaiko_d[goods]
    return f"在庫が削除されました。在庫一覧: {zaiko_d}"
  
  else:
    print("在庫の削除をキャンセルしました。")

print(zaiko_manage())
print(zaiko_append())
print(zaiko_delete())
"""

"""
#シフトスケジューラー
from datetime import date, datetime
shift_schedule = {}

def shift_day():
  shift_day = int(input("1ヶ月に何回入ってる？: "))
  for _ in range(shift_day):
    date_str = input("日にちを入力: ")
    try:
      date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()
      day = date_obj.strftime("%A")
      shift_schedule[date_obj] = day
    except ValueError:
      print("日にちの形式が間違ってるからもう一回試してみて。")

  return f"今月のシフトは: {shift_schedule}"

#シフト増やす
def shift_append():
  shift_append_question = input("シフト増やす？ y/n: ")
  if shift_append_question == "y":
    date_str = input("ふやす日にちを入力: ")
    try:
      date = datetime.strftime(date_str, "%Y-%m-%d").date()
      day = input("曜日を入力: ")
      if date in shift_schedule:
        print("上書きします。")
      shift_schedule[date] = day
      return f"シフトがふえました！ {shift_schedule}"
    except ValueError:
      return "日付の形式が間違ってるよ！"
  else:
    return f"そのままになりました！"

#シフト休む  
def shift_delete():
  shift_delete_question = input("シフト休む？ y/n: ")
  if shift_delete_question == "y":
    try:
      date_obj = datetime.strptime(date, "%Y-%m-%d").date()
      if date in shift_schedule:
        del shift_schedule[date_obj]
        return f"シフトが減りました！: {shift_schedule}"
      else:
        return "その日はシフトないよ！"
    except ValueError:
      return "日付の形式が間違ってるよ！"
  else:
    return f"そのままになりました！"

def print_sorted_schedule():
  sorted_dates = sorted(shift_schedule.keys())
  sorted_shift = {d: shift_schedule[d] for d in sorted_dates}
  print(f"今月のシフト（日付順）: {sorted_shift}") 


print("今月のシフト")
print(shift_day())
print(shift_append())
print(shift_delete())
print(f"今月のシフト: {shift_schedule}")
"""

"""
#売上高ツール
uriage_d = {}
tanka = int(input("単価を入力: "))

def uriage_manage():
  for month in range(1, 13):
    volume = int(input(f"{month}月の販売数量を入力: "))
    total_urigae = tanka * volume
    uriage_d[month] = total_urigae
  return f"売上高一覧: {uriage_d}, 年単位: {sum(uriage_d.values())}円"

def tanka_up():
  global tanka
  tanka_up_question = input("単価を上げますか? y/n: ")
  
  if tanka_up_question == "y":
    tanka_up_howmuch_question = int(input("何倍にしますか？: "))
    tanka *= tanka_up_howmuch_question
    return f"単価が{tanka_up_howmuch_question}倍になりました。単価: {tanka * tanka_up_howmuch_question}円"
  
  else:
    return f"そのままになりました。単価: {tanka}円"
  
def tanka_down():
  global tanka
  tanka_down_question = input("単価を下げますか？ y/n: ")
  if tanka_down_question == "y":
    tanka_down_howmuch_question = int(input("何円下げますか？: "))
    tanka -= tanka_down_howmuch_question
    return f"単価が{tanka_down_howmuch_question}円分下がりました。現在の単価: {tanka - tanka_down_howmuch_question}円"
  else:
    return f"そのままになりました！"

def total_uriage():
  if not uriage_d:
    return "売上データがありません。"
  return f"最終売上: {sum(uriage_d.values())}円"

print(uriage_manage())
print(tanka_up())
print(tanka_down())    
print(total_uriage())
"""
"""
import datetime as datetime
#now = datetime.datetime.now()
# print(now)

today = datetime.datetime.today()
print(today)
"""
"""
#試合ごとに判定をするツール
rma_d = {}

def player_tool():
  games = int(input("何試合分記録する？: "))
  player = input("選手名を入力: ")
  goals_list = []
  for game in range(1, games+1):
    game = int(input(f"{game}試合目のゴール数を入力: "))
    goals = int(input("ゴール数を記録: "))
    goals_list.append(goals)
    rma_d[player] = goals
    total_goals = goals_list
  return f"{player}の今季ゴール数: {total_goals}Gooooooooooal！"

def player_goals_judge():
  goal_reaction = ["Perfect", "Great", "Good", "Bao"]
  player = input("判定する選手を入力: ")
  if player in rma_d: 
    g = input("ゴール数を判定しますか? y/n :")
    if g == "y":
      print("判定を始めます。")
      player = input("選手を入力してください: ")
      judge_game = int(input("何試合目を入力しますか: "))
      goal_list = rma_d[player]
      if 1 <= judge_game <= len(goal_list):
        goals = goal_list[judge_game - 1]
        if goals >=3:
          return f"{player}はハットトリック以上！素晴らしいです。判定: {goal_reaction[0]}"
        elif goals == 2:
          return f"{player}はあいかわらずすばらしい！ 判定: {goal_reaction[1]}"
        elif goals == 1:
          return f"{player}の判定: {goal_reaction[2]}"
        else:
          return f"{player}はノーゴール！ 判定: {goal_reaction[3]}"
      else:
        return "その試合数は記録されていません。"
    else:
      return "判定を中止します。"
  else:
    return "選手記録がありません。"
print(player_tool())
print(player_goals_judge())
""" 
"""
#種別おみくじ
import random
shubetu_list = []
trains_stops = {
  "各駅停車": ["蘇我", "千葉みなと", "稲毛海岸", "検見川浜", "海浜幕張", "幕張豊砂", "新習志野", "南船橋", "二俣新町", "市川塩浜", "新浦安", "舞浜", "葛西臨海公園", "新木場", "潮見", "越中島", "八丁堀", "東京"],
  "快速": ["蘇我", "千葉みなと", "稲毛海岸", "検見川浜", "海浜幕張", "南船橋","新浦安", "舞浜","新木場", "八丁堀", "東京"], 
  "特急": ["蘇我", "海浜幕張", "東京"]
  }

n = int(input("何種類登録する？: "))
def train_shubetu():
  for i in range(1, n+1):
    train = input(f"{i}種類目: ")
    if train in trains_stops:
      shubetu_list.append(train)
    else:
      print(f"{train}は種類外です。")
  return shubetu_list


def shubetu_omikuji():
  if not shubetu_list:
    return "先に種別を尊くしてね"
  train_omikuji = random.choice(shubetu_list)
  stops = trains_stops[train_omikuji]
  fortunes = [
    "今日はラッキーだけどお金が...", 
    "各駅よりは早く着きそう！",
    "学校に遅れそう..."
    ]
  fortune = random.choice(fortunes)
  return f"おみくじの結果: {train_omikuji} 停車駅: {stops} 運勢: {fortune}"
  
print("登録種別: ", train_shubetu())
print(shubetu_omikuji())
"""

"""
# 対戦相手を入力してもらい、結果を表示するツール
import random
real_madrid = []
la_liga_teams = [
  "バルセロナ", "レアル・マドリード", "ビジャレアル", "アトレティコ・マドリード", "エスパニョール", "ベティス", "ビルバオ", "セルタ", "セビージャ", "ヘタフェ", "エルチェ", "アラベス", "ラージョ", "マジョルカ", "ソシエダ", "オサスナ", "バレンシア", "ジローナ", "オビエド", "レバンテ"
] #2025-12-17現在

def real_players():
  players = int(input("何人登録する？: "))
  for player in range(1, players+1):
    p = input(f"{player}人目の選手: ")
    real_madrid.append(p)
  return f"選手リスト: {real_madrid}"

def real_madrid_battles():
  battle_team_question = int(input("好きな数字を教えて！（0 ~ 19）: "))
  try:
    battle_team = la_liga_teams[battle_team_question]
    reactions = {
      "バルセロナ": "エル・クラシコ！",
      "レアル・マドリード": "同じチームなのでスキップ", 
      "ビジャレアル": "まぐれで3位にいるのでボコしまーす！",
      "アトレティコ・マドリード": "マドリードダービー！",
      "ソシエダ": f"{la_liga_teams[14]}のタケに要警戒！"
    }
    if battle_team in reactions:
      return reactions[battle_team]
    else:
      if real_madrid:
        overkill_player = random.choice(real_madrid)
        return f"{overkill_player}がオーバーキルしてくれる！"
      else:
        return "選手登録してね"
  except IndexError:
    return "数字が範囲外だよ！"

print(real_players())
print(real_madrid_battles())
"""
"""
#モンストダメージ計算ツール
character_atks = []
multipliers = {
    '超ダメージウォール': {'Y': 1.3, 'N': 1.0},
    'マインスイーパー': {'None': 1.0, 'N': 1.5, 'M': 2.0, 'L': 2.5, 'EL': 3.0},
    '魔法陣ブースト': {'None': 1.0, 'N': 1.5, 'M': 2.0, 'L': 2.5},
    'キラー': {'None': 1.0, 'S': 1.25, 'N': 1.25, 'M': 2.0, 'L': 2.5, 'EL': 3.0},
    '底力': {'None': 1.0, 'S': 1.25, 'N': 1.5, 'M': 2.0, 'L': 2.5, 'EL': 3.0}
}
worp_num = int(input("ワープの数を入力: "))

def get_atks():
  character_atks.clear()
  for i in range(1, 5):
    name = input(f"{i}番目のキャラを入力: ")
    atk = int(input(f"{name}の攻撃力: "))
    character_atks.append(atk)
  return f"編成の攻撃力: {character_atks}"

def get_multiplier(ability):
  levels = multipliers[ability]
  level = input(f"{ability}の等級(Y/N or None/S/N/M/L/EL) ").upper()
  if level == 'Y':
    level = 'Y'
  elif level == 'NONE':
    level = 'NONE'
  return levels.get(level, 1.0)

def calc_total_damage():
  get_atks()

  total_mult = 1.0
  total_mult *= get_multiplier('超ダメージウォール')
  total_mult *= get_multiplier('マインスイーパー')
  warp_mult = 1 + worp_num * 0.05 if input("超ワープ y/n: ").upper() == 'y' else 1.0
  total_mult *= warp_mult
  total_mult *= get_multiplier('魔法陣ブースト')
  total_mult *= get_multiplier('キラー')
  total_mult *= get_multiplier('底力')

  damages = [atk * total_mult for atk in character_atks]
  total_damage = sum(damages)

  print(f"総倍率: {total_mult:.2f}倍 (ワープ分: {warp_mult:.2f}倍)")
  print("各体ダメージ: ", damages)
  return f"合計ダメージ: {int(total_damage)}"
print(calc_total_damage())
"""

"""
#マッチングアプリ風ツール
import random
boy = input("名前を入力: ")
boy_tall = int(input("身長を入力: "))
man_blood = input("血液型を入力(A/B/O/AB): ")


girl_blood = ["O", "A", "B", "AB"]
girls = [
  {'名前': 'みお', '身長':random.randint(150, 170), '血液型': random.choice(girl_blood), '在住地': '千葉'},
  {'名前': 'あおい', '身長':random.randint(150, 170),  '血液型': random.choice(girl_blood), '在住地': '北海道'},
  {'名前':'なお', '身長': random.randint(150, 170),  '血液型': random.choice(girl_blood), '在住地': '大阪'},
  {'名前': 'あいり', '身長':random.randint(150, 170),  '血液型': random.choice(girl_blood), '在住地': '神奈川'},
  {'名前': 'けい', '身長':random.randint(150, 170),  '血液型': random.choice(girl_blood), '在住地': '東京'},
]

#男性の条件と女性（辞書）に応じてマッチングさせていく

def matching():
  girl_name = input("指名したい女性を入力（めい/あおい/なお/あいり/けい）: ").lower()
  selected_girl = next((g for g in girls if g['名前'].lower() == girl_name), None)

  if not selected_girl:
    return "正しい指名者をご入力ください。"
  
  girl_tall = selected_girl['身長']
  print("マッチングを始めます。")
  
  #身長差から診断

  height_diff = boy_tall - girl_tall
  if height_diff < 0:
    question = input(f"女性より{abs(height_diff)}cm分身長が低いです。よろしいでしょうか？ y/n: ").upper()
    if question == "Y":
      return f"マッチング成立しました！ お相手は{selected_girl['名前']}さんになりました！"
    else:
      return "マッチングがキャンセルされました。"
  elif height_diff >= 15:
    question_tall = input(f"理想の身長差です 身長差:{height_diff}cm マッチングしますか？ y/n: ").upper()
    if question_tall == 'Y':
      return f"マッチング成立しました！ お相手は{selected_girl['名前']}さんになりました！"
    else:
      return "マッチングがキャンセルされました。"
  else:
    return "マッチングがキャンセルされました。"


print(matching())
"""   

"""
#名鉄（犬山線）の停車駅一覧ツール
inuyama_line_trains = {
 "各駅停車" : {
  "停車駅": ["栄生", "東枇杷島", "下小田井", "中小田井", "上小田井", "西春", "徳重・名古屋芸大", "大山寺", "岩倉", "石仏", "布袋", "江南", "柏森", "扶桑", "木津用水", "犬山口", "犬山", "犬山遊園", "新鵜沼"], 
  "発車時間（日中時間帯、各駅停車）": [1, 17, 31, 47], 
  "color（l）": "水色",
  "answer": "準急が止まらない東枇杷島、下小田井、中小田井、徳重・名古屋芸大、大山寺をご利用のお客様"
  },

  "準急" : {
  "停車駅": ["栄生", "上小田井", "西春", "岩倉", "石仏","布袋", "江南", "柏森", "扶桑", "木津用水", "犬山口", "犬山", "犬山遊園", "新鵜沼"],
  "発車時間（日中時間帯、準急）": [11, 41], 
  "color（se）": "緑",
  "answer": "扶桑までお急ぎのお客様",
  },

  "急行":{
  "停車駅": ["栄生", "上小田井", "西春", "岩倉", "布袋", "江南", "柏森", "扶桑", "犬山", "犬山遊園", "新鵜沼"],
  "発車時間（日中時間帯、急行）": [29, 59],
  "color（E）": "緑",
  "answer": "布袋までと犬山までお急ぎのお客様"
  }, 
  
  "快速特急":{
  "停車駅": ["岩倉", "江南", "柏森", "犬山", "犬山遊園", "新鵜沼"],
  "発車時間（日中時間帯、快速特急）": [23, 53], 
  "color（re）": "緑",
  "answer": "岩倉、江南、犬山方面へお急ぎのお客様"
  
  },
  
  "ミュースカイ": { 
  "停車駅": ["岩倉", "江南", "犬山", "犬山遊園", "新鵜沼"], 
  "発車時間": [740, 808, 913, 1806, 1906, 2006, 2106,  2206], 
  "color（µ）": "緑",
  "answer": "450円（特急料金）を事前にお支払いください。"
  }
}

target_station = ""

answer = {
    "各駅停車": "準急が止まらない東枇杷島、下小田井、中小田井、徳重・名古屋芸大、大山寺をご利用のお客様",
    "準急": "扶桑までお急ぎのお客様",
    "急行": "布袋までと犬山までお急ぎのお客様",
    "快速特急": "岩倉、江南、犬山方面へお急ぎのお客様", 
    "ミュースカイ": "450円（特急料金）を事前にお支払いください。"
  }


target_station = input("目的地の駅を入力してください: ")
def meitetsu_nagoya_use():
  print("迷宮・名鉄名古屋駅へようこそ！")
  print("この駅は自動放送が流れません。")
  use_question = input("犬山方面においでですか？ y/n: ").lower()
  if use_question == "y":
      return "名鉄線をご利用ください。"
  else:
    return "ただいま名鉄犬山線のみ対応しております。岐阜、豊橋方面実装までしばらくお待ちください。"

def maitetsu_train_judge():
  global target_station
  target_station  = input("目的地の駅を入力してください。: ")
  all_stations = set()
  for train in inuyama_line_trains.values():
    all_stations.update([s for s in train["停車駅"]])
    if target_station not in all_stations:
      return "申し訳ございません。ただいま犬山線の駅のみ対応しております。"
    else:
      return "ご利用ありがとうございます！検索しております..."
#ミュースカイを使うか聞く
def µ_sky_use():
  µ_sky = input("ミュースカイをご利用ですか？ y/n: ").lower()
  if µ_sky == "y":
    time = int(input("STEP1 ご利用の時間を選択してください（740/808/913/1806/1906/2006/2106/2206、:なし）。："))
    if time not in inuyama_line_trains["ミュースカイ"]["発車時間"]:
      return "申し訳ございません。只今の時間はミュースカイは名古屋止まりになっています。犬山方面にお急ぎでしたら、快速特急をご利用ください。"
    get_off_staton = input("STEP2 下車される駅を選択してください（岩倉/江南/犬山/犬山遊園/新鵜沼）: ")
    if get_off_staton not in [s for s in inuyama_line_trains["ミュースカイ"]["停車駅"]]:
      return "停車駅をご確認ください。" 
  else:
    return "ご利用をキャンセルしました。"

def train():
  global target_station
  if not target_station:
    return "駅名を入力してください。"
  

  recommended = None
  for type_nane, data in inuyama_line_trains.items():
    if target_station in [s for s in data["停車駅"]]:
      recommended = type_nane
      break

    if recommended:
      return f"{data['answer']}"
    else:
      return "正しい犬山線の駅名を入力してください。"

print(meitetsu_nagoya_use())    
print(maitetsu_train_judge())
print(µ_sky_use())
print(train())
"""

"""
#東海道新幹線ツール
tokaido_shinkansen = {
  "こだま": {
    "停車駅": ["品川", "新横浜", "小田原", "熱海", "三島", "新富士", "静岡", "掛川", "浜松", "豊橋", "三河安城", "名古屋"],
    "発車時間（日中時間帯）": [27, 57]
  },

  "ひかり" : {
    "停車駅": ["品川", "新横浜", "小田原", "熱海", "静岡", "浜松", "豊橋", "名古屋"],
    "発車時間（発車時間帯）" : [3, 33]
  },

  "のぞみ": {
    "停車駅": ["品川", "新横浜", "名古屋"],
    "発車時間": [00, 9, 12, 21, 30, 42, 48]
  }
}

target_station = ""
def shinkansen_use():
  global target_station
  target_station = input("目的地の駅を入力してください。: ").lower()
  all_stations = set()
  for train in tokaido_shinkansen.values():
    all_stations.update([s.lower() for s in train["停車駅"]])
  if target_station not in all_stations:
    return "正しい駅名を入力してください。"
  elif target_station == "品川":
    return "在来線をご利用ください。"
  else:
    return "ご利用ありがとうございます！"

def shinkansen_search():
  global target_station
  if not target_station:
    return "駅名を入力してください。"
  recommended = None
  for type_name in ["のぞみ", "ひかり", "こだま"]:
    if target_station.lower() in [s.lower() for s in tokaido_shinkansen[type_name]["停車駅"]]:
      recommended = type_name
      break
  
  if recommended == "のぞみ":
    return "名古屋へお急ぎのお客様はのぞみをご利用ください。"
  elif recommended == "ひかり":
    return "のぞみが止まらない駅でこだまよりお急ぎの方はひかりをご利用ください。"
  elif recommended == "こだま":
    return "こだまをご利用ください。"
  else:
    return "正しく駅名を入力してください。"
  
print(shinkansen_use())
print(shinkansen_search())
""" 


#レアル・マドリードの選手に応じて2026WCで応援する代表を表示させる神ツール
#2025-12-23現在の選手のステータス
real_madrid = {
  "Mbappé": {
    "number": 10, "goals": 18, "from": "France", "position": "FW"
    },
  "Güler": {
    "number": 15, "goals": 3, "from": "Turkey", "position": "FW"
    },
  "Vinicius": {
    "number": 7, "goals": 5, "from": "Brazil", "position": "FW"
    },
  "Bellingham": {
    "number": 5, "goals": 4, "from": "England", "position": "MF"
    }, 
  "Coutois": {
    "number": 1, "goals": 0, "from": "Belgium", "position": "GK"
    },
  "Carvajal": {
    "number": 2, "goals": 0, "from": "Spain", "position": "DF"
    },
  "Rodrigo": {
    "number": 11,  "goals": 1, "from": "Brazil", "position": "FW"
    },
  "Valverde": {
    "number":8, "goals": 0, "from": "Uruguay", "position": "MF"
    },
  "Camavinga": {
    "number": 6, "goals": 1, "from": "France", "position": "MF"
    },
  "Tchouaméni": {
    "number": 14, "goals": 0, "from": "France", "position": "MF"
    },
  "Arnold": {
    "number": 12, "goals": 0, "from": "England", "position": "DF"
  }
}

favorite_player = ""
def player_registration():#選手登録
  global favorite_player
  favorite_player = input("好きな選手を入力してください: ()").lower()
  all_players = set()
  for plyaer in real_madrid.keys():
    all_players.add(plyaer.lower())
  

def player_country_support():
  global favorite_player
  if favorite_player not in real_madrid:
    return "その選手はレアル・マドリードにいません。正しい名前を入力し。"
  else:
    coutry = real_madrid[favorite_player.capitalize()["from"]]
    return f"来年のワールドカップで{favorite_player}がいる{coutry}代表を応援しましょう！"

print(player_registration())
print(player_country_support())
  






"""
変数のスコープって何？
→ 「変数はどこまで生きてるか？」 の話
関数の中と外で別世界だと思ってくれ！
"""

"""
#Mbappで即実践
team = "RMA"
def celebrate():
  player = "Mbappé"
  print(f"{player}がゴーーーーーーーーーーーーーール！{team}最高！")

celebrate()
print(team)
"""

"""
#やらかしパターン（paizaで100%出る）
x = 10
def func():
  x = 20
  print(x)
func()
print(x)
"""

"""
#正しくグローバル変数をいじる方法
money = 0
def add_wage(wage):
  global money
  money += wage
add_wage(5000)
add_wage(6000)

print(money)
"""

"""
#今日のミニ課題
#セブン給料シミュレーション
total = 0
def work(hours):
  global total
  total += hours * 1140
  print(f"今日の給料: {hours * 1140}")

work(5)
work(6.5)
print(f"今月の給料: {int(total)}円")
"""

"""
#paiza対策（超出る）
#グローバル変数でカウンターを作る問題とか
count = 0
def check(num):
  global count
  if num % 2 == 0:
    count += 1
  return "偶数" if num % 2 == 0 else "奇数"

#使う
n = int(input())
for _ in range(n):
  x = int(input())
  print(check(x))
print(f"偶数の数: {count}個")
"""

#今やったやつをレアル風にしてみた
team_score = 0 #グローバル変数（チーム通算）

def match():
  match_goals = 0 #ローカル（この試合だけ）

  def Mbappé_shot(): #（試合の中のシュート関数）
    nonlocal match_goals #１つ外側のmatch_goalsを使う宣言
    match_goals += 1
    global team_score #一番外側のteam_scoreを使う宣言
    team_score += 1
    print("Mbappéがゴーーーーーーーーール！！！！！！")

    #試合シミュレーション
    Mbappé_shot(1)
    Mbappé_shot(1)
    print(f"この試合: {match_goals}ゴール")
    print(f"今季通算: {team_score}ゴール")

match()
print(f"最終通算: {team_score}ゴール")




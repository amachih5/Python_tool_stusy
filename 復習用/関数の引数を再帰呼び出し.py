"""
再帰って何？（1行で）
→ 関数が自分自身を呼ぶだけ！
「俺が俺を呼ぶ」みたいなやつ😂
"""

"""
#カウントダウン
def countdown(n):
  if n <= 0:
    print("ゴーーーーーーーーーーーーーーーーーーーーーーーール⚽️！！！！")
  else:
    print(n)
    countdown(n-1)
countdown(5)
"""

"""
#今日の神例（paizaで9割出る階乗）
def kaijo(n):
  if n == 0 or n == 1:
    return 1
  else:
    return n * kaijo(n - 1)
print(kaijo(5))
"""

"""
#今日のミニ課題
# Mbappéが何連続ゴール決めるかシミュ
def Mbappé_goals(streak):
  if streak == 0:
    print("試合終了！")
  else:
    print(f"Mbappéが{streak}試合連続ゴール！")
    Mbappé_goals(streak - 1)
Mbappé_goals(7)
"""

import math
def combo_attacks(n):
  return math.factorial(n) // math.factorial(2) * math.factorial(n - 2)
print(combo_attacks(11))
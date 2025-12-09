"""
#1.リスト内包表記
li10 = [i ** 2 for i in range(1, 11) if i % 2== 0]
print(li10)
"""

"""
#2.n人分入力
n = int(input())
#n人分の名前とゴール数を取る
d = {}

for _ in range(n):
  name = input("名前を入力: ")
  goals = int(input("ゴール数を入力: "))
  d[name] = goals
print("完成系: ", d)


#関数と再起呼び出し
def total_number(n):
  n = int(input())
  for t in range(1, n):
    total = sum(t)
    return total
print(total_number(5))
"""
#4.クラスと継承





"""
#5.例外処理
import math
n = int(input())
try:
  total = math.factorial(n)
  print(total)
except ValueError:
  print("数字入れて！")
"""
"""
#2問目（n人分入力 + 辞書）
n = int(input("何人分のデータを入れますか?: "))

monster_dict = {}
for _ in range(n):
  name = input("モンスター名: ")
  hp = int(input("HP: "))
  monster_dict[name] = hp
print("完成系:",monster_dict)
"""

"""
#再帰呼び出し
def total_number(n):
  if n <= 0:
    return 0
  else:
    return n + total_number(n-1)
print(total_number(5))
"""

"""
#例外処理 + モジュール
import math
try:
  n = int(input("年齢を入れて: "))
  total = math.factorial(n)
  print(total)
except ValueError:
  print("数字を入れて！")
"""
"""
try:
  num = int(input("数字を入れて: "))
  print(100/num)
except ZeroDivisionError:
  print("数字じゃないよ！")
finally:
  print("計算完了！")
"""
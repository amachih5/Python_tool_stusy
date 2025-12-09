#name = input()
#print("こんにちは"+ name)

"""
name = input("名前を入力: ")
age = int(input("年齢を入力: "))
print(f"{name}さんは{age}歳です。")
"""

"""
number = int(input("Mbappéの背番号は？: "))
if number == 9:
  print("正解！レアルのエースだ！")
else:
  print(f"残念、正解は9だよ（入力したのは{number}）")
"""


"""
name = input("名前: ")
hours = int(input("今日の労働時間: "))
wage = int(input("時給を入力: "))
money = hours * wage
print(f"{name}さんの今月の給料は{money}円だ！")
"""

"""
n = int(input())
numbers = list(map(int, input().split()))
print(sum(numbers))
"""
"""
#複数行の数字を一気にリストにぶち込むパターン
n = int(input()) #行数を聞く
li = [0] * n
# [0] * 5 って書くと → [0, 0, 0, 0, 0] が一瞬で作れる
# つまり「n個の0が入ったリスト」を先に作ってるだけ！
# 後で上書きするから中身が0でも何でもOK
# （[None]*n とか [""]*n でも同じことできる）

for i in range(n): #行数分繰り返す
  li[i] = int(input()) #1行ずつもらう
  # 1回目 → li[0] に次の入力入れる
  # 2回目 → li[1] に次の入力入れる
  # …って感じで全部埋まる
print(li)
"""
"""
#内包表記
n = int(input())
li = [int(input()) for _ in range(n)]
#短くなる
"""
"""
まとめ

[0] * n → 長さnのリストを一瞬で作る神テク
その後forで1行ずつ上書きしてるだけ
paiza/AtCoderの9割の問題がこのパターン!
"""

"""
n = int(input())
li = [[int(x) for x in input().split()] for _ in range(n)]
print(li)
"""
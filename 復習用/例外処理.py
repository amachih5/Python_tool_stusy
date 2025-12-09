"""
#今日11/26 残りミッション（例外処理💀）
def mbappe_quiz():
  while True:
    try:
      guess = int(input("Mbappéの背番号は？: "))
      if guess == 9:
        print("正解！エースすぎる！⚽️")
        break
      else:
        print(f"残念！正解は9だよ！（入力: {guess}）")
    except ValueError:
      print("数字を入れてくれ！「9」って打ってみて！")

mbappe_quiz()
"""
"""
#時給計算 変な入力されても死なない版
def safe_calc():
  try:
    hours = float(input("今日は何時間働いた？: "))
    if hours < 0:
      print("マイナス時間とかありえねぇ！")
      return
    pay = hours * 1140
    print(f"今日の給料: {int(pay)}円！")
  except ValueError:
    print("ちゃんと数字を入れてくれよ！")

safe_calc()
"""


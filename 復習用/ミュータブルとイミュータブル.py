#今日の神例
#goals_list = [10, 30, 25]
#goals_list[0] = 50
#print(goals_list)
"""
player = ("Mbappé", 10) #タプルは変更不可
#player[1] = 7 #エラー！背番号は変えられない
player = ("Vinicius", 7) #丸ごと新しく作るしかない
print(player)
"""


def test(lst):
  lst.append(999) #ミュータブルは関数内で変えても外に影響する！

my_goals = [10, 100]
test(my_goals)
print(my_goals)

def test2(t): #イミュータブルは関数内で変えても外に影響なし
  t = (1, 2, 3)

my_tuple = (10, 20)
test2(my_tuple)
print(my_tuple)


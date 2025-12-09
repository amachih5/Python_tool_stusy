"""
覚えとけポイント

順番: [処理 for ... if ...] または [処理 if ... else ... for ...]
ネスト: 2重もできるけど今は無視（例: [[0 for _ in range(3)] for _ in range(3)] → 3x3行列）
エラー注意: ifだけなら後ろ、elseあるなら前!
"""

"""
tens = [i * 10 for i in range(1, 6)]
print(tens)

shifts = ["休み" if i >= 6 else "出勤" for i in range(1, 6)]
print(shifts)
"""

"""
#Mbappéのゴール数シミュ → 0〜10試合で5ゴール以上なら「活躍」リスト
Mbappé_goals = ["活躍" for goals in range(0, 11) if goals >= 5]
print(Mbappé_goals)
"""

import random
goals_list = [random.randint(0, 10) for _ in range(10)]
result = ["活躍" if g >= 5 else "普通" for g in goals_list]
print("ゴール:",goals_list)
print("評価:", result)
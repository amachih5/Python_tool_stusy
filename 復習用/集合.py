"""
集合（set）って何？
→ 重複なしのリストみたいなやつ！
paizaで「ユニークな数字だけ抜き出せ」みたいな問題9割これ！
"""

#goals = ["Mbappé", "Vinicius", "Mbappé","Bellingham","Mbappé"]

"""
#集合にぶち込む → 重複消える！
unique_scores = set(goals)
print(unique_scores)

# 追加
unique_scores.add("Rodrygo")
print(unique_scores)

#削除
unique_scores.remove("Vinicius")
unique_scores.discard("誰か知らん人")
"""

"""
#数学みたいに使える（これがpaizaで出まくる）
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a & b)
print(a | b)
print(a - b)
"""

"""
今日のミニ課題

orders = ["おにぎり", "コーヒー", "弁当", "おにぎり", "タバコ", "コーヒー"]

unique_orders = set(orders)
print(f"今日の商品種類: {len(unique_orders)}種類! → {unique_orders}")
"""

#やったことまとめ

#今季レアルでゴールを決めた選手セット
rma_scorers = {"Mbappé", "Vinicius", "Bellingham", "Rodrygo"}

#バルサのスコラー
barça_scorers = {"Lewandowski", "Yamal", "Raphinha"}

#1. in →いるかチェック
print("Mbappé" in rma_scorers)

#2. == → 完全に同じか
print(rma_scorers == {"Mbappé", "Vinicius", "Bellingham", "Rodrygo"})

# 3. <= >= → 部分集合・全体集合
print({"Mbappé", "Vinicius"} <= rma_scorers)

# 4. ^ → 対称差（どっちか片方だけにいるやつ）
print(rma_scorers ^ barça_scorers)

# 5. 内包表記で集合生成（はやとがやった神テク）
# 0〜20でゴール数シミュ → 10ゴール以上の選手だけ集合にする
high_scorers = {f"選手{i}" for i in range(21) if i >= 10}
print(high_scorers)
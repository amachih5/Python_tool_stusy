"""
クラスって何？（1行で）
→ 選手を「データ＋行動」をセットでまとめる箱
Mbappéを「名前・背番号・ゴール数」＋「シュートする」ってまとめる神テク！
"""

"""
#Mbappéで即実践
class Player:
  def __init__(self, name, number): #作った瞬間に呼ばれる
    self.name = name #self = 自分自身
    self.number = number
    self.goals = 0 #最初は0ゴール

  def shoot(self):
    self.goals += 1
    print(f"{self.name}がゴーーーーーーーーーーーール！！今季{self.goals}ゴール目⚽️")

mbappe = Player("Mbappé", 9)
vinicius = Player("Vinicius", 7)

mbappe.shoot()
mbappe.shoot()
vinicius.shoot()
"""

"""
#店員クラスを作れ！
class Staff:
  def __init__(self, name):
    self.name = name
    self.wage_total = 0
  
  def work(self, hours):
    pay = hours * 1140
    self.wage_total += pay
    print(f"{self.name}さんは今日{hours}時間働いて{pay}円！お疲れ！")
  
hayato = Staff("はやと")
hayato.work(5.5)
hayato.work(8)
print(f"今月の給料合計: {hayato.wage_total}円！")
"""

class Player:
  def __init__(self, name, number):
    self.name = name
    self._number = number
    self.__secret_goals = 50

  def shoot(self):
    self.__secret_goals += 1
    print(f"{self.name}がゴーーーーーール！！表向きは{self._number}番")

mbappe = Player("Mbappé", 10)
mbappe.shoot()
print(mbappe.name)
print(mbappe._number)

print(mbappe._Player__secret_goals)
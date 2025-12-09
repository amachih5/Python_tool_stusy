""""
#Mbappéで即実践
#親クラス（基本の選手）
class Player:
  def __init__(self, name, number):
    self.name = name
    self.number = number
    self.goals = 0

  def shoot(self):
    self.goals += 1
    print(f"{self.name}がゴーーーーーーーーーーーール！！今季{self.goals}ゴール目！")

#子クラス（ストライカーは親の全部＋ハットトリック機能付き！）
class Striker(Player): # ←ここで継承！
  def hattrick(self):
    self.goals += 3
    print(f"{self.name}がハットトリック！！一気に+3ゴール！⚽️⚽️⚽️")

mbappe = Striker("Mbappé", 10)
mbappe.shoot()
mbappe.shoot()
mbappe.hattrick()

print(f"最終ゴール数: {mbappe.goals}")
"""

#今日のミニ課題（セブン辞め対策）
#普通の店員
class SevenStaff:
  def __init__(self, name):
    self.name = name 
    self.wage_total = 0

  def work(self, hours):
    pay = hours * 1140
    self.wage_total += pay
    print(f"{self.name}さん、今日{hours}時間で{pay}円！")

#もうすぐやめる店員の僕
class Hayato(SevenStaff):
  def quit(self):
    print(f"{self.name}さんはもうすぐバイトを辞めます！")

me = Hayato("はやと")
me.work(8)
me.work(5.5)
me.quit()

print(f"最終給料: {me.wage_total}円！")
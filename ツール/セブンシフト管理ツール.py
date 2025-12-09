import pandas as pd

def safe_input(prompt, type_func=float): #例外処理付き関数
  while True:
    try:
      return type_func(input(prompt))
    except ValueError:
      print("ちゃんと入力してくれよ！")

class ShiftManager:
  def __init__(self):
    self.shifts = {}
  
  def add_shift(self, name, hourly, hours):
    pay = hourly * hours
    self.shifts[name] = [hourly, hours, pay]

  def total_pay(self):
    return sum([data[2] for data in self.shifts.values()])
  
  def save_to_excel(self):
    data = {"名前": [], "時給": [], "労働時間": [], "給料": []}
    for name, info in self.shifts.items():
      data["名前"].append(name)
      data["時給"].append(info[0])
      data["労働時間"].append(info[1])
      data["給料"].append(info[2])
    
    df = pd.DataFrame(data)
    df.to_excel("セブンシフト_2025_12.xlsx", index=False)
    print("Excel保存完了！！")

manager = ShiftManager()
n = int(input("何人分入力?: "))
for _ in range(n):
  name = input("名前: ")
  hourly = safe_input("時給: ",int)
  hours = safe_input("労働時間: ", float)
  manager.add_shift(name, hourly, hours)

print("シフトデータ", manager.shifts)
print("合計給料: ", manager.total_pay(), "円！")
manager.save_to_excel()
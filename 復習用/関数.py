"""
def year_salary(day, hours, hours_per_wage, sinya_teate=0, zangyoudai=0,zangyou_time=0, zeikin=0):
  month_wage = day * hours * hours_per_wage
  sinya_teate = hours_per_wage * 1.25
  zangyoudai = hours_per_wage * 1.25 * zangyou_time
  bonus = sinya_teate + zangyoudai
  tax = zeikin
  total_year_salary = month_wage * 12 + bonus - tax
  if total_year_salary == 4000000:
    return "へいきん"
  elif total_year_salary >= 10000000:
    return "あなたは日本の人口の1%以内に入りました！"
  else:
    return "もっと働きましょう"
print(year_salary(22, 22, 1000000))
"""
"""
#関数の作り方
def goal_celebrate(name):
  return f"{name}がゴーーーーーーーーーーーーーーーーーーーーーーール⚽️！！！"
print(goal_celebrate("Mbappé"))
print(goal_celebrate("Vinicius"))
"""

"""
#給料計算関数（セブン辞め対策）
def calc_wage(hours, hourly=1150):
  return hours * hourly

print(calc_wage(5.5))
print(calc_wage(6, 1200))
"""

"""
#Mbappéのゴール数から評価返す関数
def mbappé_check(goals):
  if goals >= 50:
    return "バケモン"
  elif goals >= 30:
    return "エース級"
  else:
    return "頑張りましょう"
print(mbappé_check(60))
"""

#Mbappéのゴール数から評価返す関数
def mbappé_check(goals):
  if goals >= 50:
    return "バケモン"
  elif goals >= 30:
    return "エース級"
  else:
    return "頑張りましょう"
print(mbappé_check(60))

#paiza対策（これ100%出る）
def my_max(a, b, c):
  return max(a, b, c)

n = int(input())
for _ in range(n):
  x, y, z = map(int, input().split())
  print(my_max(x, y, z))
money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить




while money_capital >= 0:
    month += 1
    spend *= (month + increase)
    total = salary - spend
    money_capital += total

print(month)


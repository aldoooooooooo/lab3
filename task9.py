salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев
new_spend = spend

for i in range(months):
    if i == 0:
        total = spend - salary
        need_money += total
    else:
        spend += (spend*increase)
        total = spend - salary
        need_money += total





print(round(need_money))


type_flowers = input()
number_flowers = int(input())
budget = int(input())
price = 0
if type_flowers == "Roses":
    if number_flowers <= 80:
        price = number_flowers * 5
    else:
        price = number_flowers * 5 * 0.9
    if price <= budget:
        money_left = budget - price
        print(f"Hey, you have a great garden with {number_flowers} {type_flowers} and {money_left:.2f} leva left.")
    else:
        need_money = abs(budget - price)
        print(f"Not enough money, you need {need_money:.2f} leva more.")
elif type_flowers == "Dahlias":
    if number_flowers <= 90:
        price = number_flowers * 3.8
    else:
        price = number_flowers * 3.8 * 0.85
    if price <= budget:
        money_left = budget - price
        print(f"Hey, you have a great garden with {number_flowers} {type_flowers} and {money_left:.2f} leva left.")
    else:
        need_money = abs(budget - price)
        print(f"Not enough money, you need {need_money:.2f} leva more.")
elif type_flowers == "Tulips":
    if number_flowers <= 80:
        price = number_flowers * 2.8
    else:
        price = number_flowers * 2.8 * 0.85
    if price <= budget:
        money_left = budget - price
        print(f"Hey, you have a great garden with {number_flowers} {type_flowers} and {money_left:.2f} leva left.")
    else:
        need_money = abs(budget - price)
        print(f"Not enough money, you need {need_money:.2f} leva more.")
elif type_flowers == "Narcissus":
    if number_flowers >= 120:
        price = number_flowers * 3
    else:
        price = number_flowers * 3 * 1.15
    if price <= budget:
        money_left = budget - price
        print(f"Hey, you have a great garden with {number_flowers} {type_flowers} and {money_left:.2f} leva left.")
    else:
        need_money = abs(budget - price)
        print(f"Not enough money, you need {need_money:.2f} leva more.")
elif type_flowers == "Gladiolus":
    if number_flowers >= 80:
        price = number_flowers * 2.5
    else:
        price = number_flowers * 2.5 * 1.2
    if price <= budget:
        money_left = budget - price
        print(f"Hey, you have a great garden with {number_flowers} {type_flowers} and {money_left:.2f} leva left.")
    else:
        need_money = abs(budget - price)
        print(f"Not enough money, you need {need_money:.2f} leva more.")




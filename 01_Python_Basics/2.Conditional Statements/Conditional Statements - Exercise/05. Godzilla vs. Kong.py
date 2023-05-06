budget = float(input())
actors = int(input())
price_clothes = float(input())
decor = budget * 0.1
if actors > 150:
    price_clothes = price_clothes - price_clothes * 0.1

total_price = actors * price_clothes + decor
if total_price <= budget:
    money_over = budget - total_price
    print(f"Action!")
    print(f"Wingard starts filming with {money_over:.2f} leva left.")
else:
    needed_money = abs(budget - total_price)
    print("Not enough money!")
    print(f"Wingard needs {needed_money:.2f} leva more.")
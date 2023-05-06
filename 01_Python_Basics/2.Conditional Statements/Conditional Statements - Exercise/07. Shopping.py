budget = float(input())
number_videocarti = int(input())
number_procesori = int(input())
number_ram = int(input())
price_videocarta = number_videocarti * 250.00
price_procesori = number_procesori * (price_videocarta * 0.35)
price_ram = number_ram * (price_videocarta * 0.1)
price = price_videocarta + price_procesori + price_ram
if number_videocarti > number_procesori:
    discount = price * 0.15
    price = price - discount
if price <= budget:
    excess = budget - price
    print(f"You have {excess:.2f} leva left!")
else:
    need_money = abs(budget - price)
    print(f"Not enough money! You need {need_money:.2f} leva more!")
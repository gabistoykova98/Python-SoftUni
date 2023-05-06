trip = float(input())
puzzles = int(input())
dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())

price = puzzles * 2.60 + dolls * 3 + bears * 4.10 + minions * 8.20 + trucks * 2.00
if puzzles + dolls + bears + minions + trucks < 50:
    price = price
else:
    discount = price * 0.25
    price = price - discount

rent = price * 0.1
profit = price - rent

if profit >= trip:
    excess = profit - trip
    print(f"Yes! {excess:.2f} lv left.")
else:
    needed_money = abs(profit - trip)
    print(f"Not enough money! {needed_money:.2f} lv needed.")



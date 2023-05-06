budget = int(input())
season = input()
people = int(input())
price = 0.00
if season == "Spring":
    if people <= 6:
        price += 3000 * 0.9
    elif 7 <= people <= 11:
        price += 3000 * 0.85
    elif people >= 12:
        price += 3000 * 0.75
elif season == "Summer":
    if people <= 6:
        price += 4200 * 0.9
    elif 7 <= people <= 11:
        price += 4200 * 0.85
    elif people >= 12:
        price += 4200 * 0.75
elif season == "Autumn":
    if people <= 6:
        price += 4200 * 0.9
    elif 7 <= people <= 11:
        price += 4200 * 0.85
    elif people >= 12:
        price += 4200 * 0.75
elif season == "Winter":
    if people <= 6:
        price += 2600 * 0.9
    elif 7 <= people <= 11:
        price += 2600 * 0.85
    elif people >= 12:
        price += 2600 * 0.75
if season != "Autumn" and people % 2 == 0:
    price *= 0.95

money_left = abs(budget - price)
if budget >= price:
    print(f"Yes! You have {money_left:.2f} leva left.")
else:
    print(f"Not enough money! You need {money_left:.2f} leva.")


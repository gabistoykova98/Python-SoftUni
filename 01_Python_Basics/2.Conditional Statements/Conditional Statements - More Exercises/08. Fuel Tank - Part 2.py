fuel = input()
liters = float(input())
card = input()

if fuel == "Gasoline":
    if card == "Yes":
        price = liters * (2.22 - 0.18)
    elif card == "No":
        price = liters * 2.22
elif fuel == "Diesel":
    if card == "Yes":
        price = liters * (2.33 - 0.12)
    elif card == "No":
        price = liters * 2.33
elif fuel == "Gas":
    if card == "Yes":
        price = liters * (0.93 - 0.08)
    elif card == "No":
        price = liters * 0.93
if 20 <= liters <= 25:
    price = price * 0.92
elif liters > 25:
    price = price * 0.90

print(f"{price:.2f} lv.")
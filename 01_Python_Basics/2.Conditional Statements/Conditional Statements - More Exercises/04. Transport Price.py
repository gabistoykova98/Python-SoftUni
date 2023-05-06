km = int(input())
time = input()
price = 0.00
taxi_rate = 0.00

if time == "day":
    taxi_rate = 0.79
else:
    taxi_rate = 0.90

if km < 20:
    price = (f"{0.70 + km * taxi_rate:.2f}")
elif km < 100:
    price = (f"{km * 0.09:.2f}")
else:
    price = (f"{km * 0.06:.2f}")

print(price)
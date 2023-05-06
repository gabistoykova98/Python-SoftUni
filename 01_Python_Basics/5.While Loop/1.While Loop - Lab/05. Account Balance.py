inpt = input()
total_money = 0

while inpt != "NoMoreMoney":
    amount = float(inpt)
    if amount < 0:
        print("Invalid operation!")
        break

    total_money += amount
    print(f"Increase: {amount:.2f}")
    inpt = input()

print(f"Total: {total_money:.2f}")
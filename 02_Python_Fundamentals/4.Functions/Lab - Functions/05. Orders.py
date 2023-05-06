def price(name, quantity):
    total = 0
    if name == "coffee":
        total += quantity * 1.50
    elif name == "coke":
        total += quantity * 1.40
    elif name == "water":
        total += quantity * 1.00
    elif name == "snacks":
        total += quantity * 2.00
    return f"{total:.2f}"


name = input()
quantity = int(input())

print(price(name, quantity))

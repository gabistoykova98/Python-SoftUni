import math

inp = input().split("|")
budget = int(input())
total = 0
new_price = []
for ind in inp:
    item = ind.split("->")
    typ = item[0]
    price = float(item[1])

    if budget > 0:
        if typ == "Clothes":
            if price > 50.00:
                continue
            else:
                budget -= price
                total += price
                new_pr_cl = (price * 1.4)
                new_price.append(new_pr_cl)
        if typ == "Shoes":
            if price > 35.00:
                continue
            else:
                budget -= price
                total += price
                new_pr_sh = int(price * 1.4)
                new_price.append(new_pr_sh)
        if typ == "Accessories":
            if price > 20.50:
                continue
            else:
                budget -= price
                total += price
                new_pr_ac = floor(price * 1.4)
                new_price.append(new_pr_ac)

total_price = total * 1.4
profit = total_price - budget

if total_price > 150:
    print(*new_price)
    print(f"Profit: {profit}")
    print(f"Hello, France!")
else:
    print(*new_price)
    print(f"Profit: {profit}")
    print(f"Not enough money.")






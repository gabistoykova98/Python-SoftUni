budget = float(input())
price_flour_kg = float(input())
price_eggs = price_flour_kg * 0.75
price_milk_l = price_flour_kg + price_flour_kg * 0.25
breads = 0
eggs = 0
price_bread = price_eggs + price_flour_kg + price_milk_l / 4


while budget >= price_bread:
    budget -= price_bread
    breads += 1
    eggs += 3
    if breads % 3 == 0:
        eggs -= (breads - 2)
print(f"You made {breads} loaves of Easter bread! Now you have {eggs} eggs and {budget:.2f}BGN left.")





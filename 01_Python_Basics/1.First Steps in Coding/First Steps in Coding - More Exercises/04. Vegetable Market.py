price_vegetables = float(input())
price_fruits = float(input())
kg_vegetables = int(input())
kg_fruits = int(input())
price_leva = kg_vegetables * price_vegetables + kg_fruits * price_fruits
price_euro = price_leva / 1.94
print(f"{price_euro:.2f}")
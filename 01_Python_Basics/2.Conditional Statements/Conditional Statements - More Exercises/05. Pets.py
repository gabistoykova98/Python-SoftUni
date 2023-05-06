import math
days = int(input())
food_kg = int(input())
food_dog = float(input())
food_cat = float(input())
food_turtle = float(input()) / 1000
need_food = days * (food_cat + food_dog + food_turtle)
if need_food <= food_kg:
    remainder_food = food_kg - need_food
    print(f"{math.floor(remainder_food)} kilos of food left.")
else:
    needed = abs(food_kg - need_food)
    print(f"{math.ceil(needed)} more kilos of food are needed.")

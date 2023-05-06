chicken_menu = int(input())
fish_menu = int(input())
vegetarian_menu = int(input())
price = chicken_menu * 10.35 + fish_menu * 12.40 + vegetarian_menu * 8.15
dessert = price * 0.2
total_price = price + dessert + 2.5
print(f"{total_price:.2f}")

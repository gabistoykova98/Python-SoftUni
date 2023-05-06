length = int(input())
width = int(input())
height = int(input())
percent = float(input())
capacity = length * width * height
capacity_liters = capacity / 1000
occupied_space = percent / 100
litters_water = capacity_liters * (1 - occupied_space)
print(litters_water)



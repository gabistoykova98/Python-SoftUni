x = float(input())
y = float(input())
h = float(input())
area_green = 2 * (x * x) + 2 * (x * y) - 1.2 * 2 - 2 * (1.5 * 1.5)
area_red = 2 * (x * y) + x * h
green_paint = area_green / 3.4
red_paint = area_red / 4.3
print(f"{green_paint:.2f}")
print(f"{red_paint:.2f}")
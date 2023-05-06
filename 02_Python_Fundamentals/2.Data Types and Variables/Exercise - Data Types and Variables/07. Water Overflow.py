capacity = 255
lines = int(input())
lit = 0
for i in range(lines):
    liters = int(input())
    if capacity < liters:
        print(f"Insufficient capacity!")
    else:
        lit += liters
        capacity -= liters
print(lit)
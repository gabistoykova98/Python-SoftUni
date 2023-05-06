delitel = int(input())
granica = int(input())
number = 0

for i in range(granica, delitel, -1):
    if i % delitel == 0:
        number = i
        break
print(number)

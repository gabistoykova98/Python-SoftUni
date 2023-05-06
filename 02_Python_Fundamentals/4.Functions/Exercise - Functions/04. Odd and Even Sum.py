num = int(input())
listt = []
listt.append(str(num))
odd = []
even = []

for i in listt:
    for ch in i:
        if int(ch) % 2 == 0:
            even.append(int(ch))
        else:
            odd.append(int(ch))

print(f"Odd sum = {sum(odd)}, Even sum = {sum(even)}")

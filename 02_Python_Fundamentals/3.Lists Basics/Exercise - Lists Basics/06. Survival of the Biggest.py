num = [int(x) for x in input().split()]
counter_to_remove = int(input())

for i in range(counter_to_remove):
    small = min(num)
    num.remove(small)


print(*num, sep=", ")

# print(', '.join(str(x) for x in num))




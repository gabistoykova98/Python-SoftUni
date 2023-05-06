string = [int(x) for x in input().split()]
for i in range(len(string)):
    if string[i] > 0:
        string[i] = -abs(string[i])
    elif string[i] < 0:
        string[i] = abs(string[i])

print(string)


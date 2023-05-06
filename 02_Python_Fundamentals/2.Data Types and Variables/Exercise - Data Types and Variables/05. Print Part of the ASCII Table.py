start = int(input())
stop = int(input())
result = []

for i in range(start, stop + 1):
    symbol = chr(i)
    result.append(symbol)

print(*result, sep= " ")



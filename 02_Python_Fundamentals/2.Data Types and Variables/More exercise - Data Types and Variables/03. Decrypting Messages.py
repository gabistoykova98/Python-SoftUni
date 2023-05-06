key = int(input())
lines = int(input())
listt = []

for i in range(lines):
    ord_letters = chr(ord(input()) + key)
    listt.append(ord_letters)

print(*listt, sep='')

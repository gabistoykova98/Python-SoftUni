import sys

inpt = input()
max = -sys.maxsize

while inpt != "Stop":
    num = int(inpt)

    if num > max:
        max = num
    inpt = input()

print(max)

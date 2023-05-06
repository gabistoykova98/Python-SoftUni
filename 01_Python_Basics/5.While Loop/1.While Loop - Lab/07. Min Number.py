import sys

inpt = input()
min = sys.maxsize

while inpt != "Stop":
    num = int(inpt)
    if num < min:
        min = num

    inpt = input()

print(min)

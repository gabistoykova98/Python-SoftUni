start = int(input())
stop = int(input())
magic_num = int(input())

found = False
counter = 0

for first in range(start, stop + 1):
    for second in range(start, stop + 1):
        counter += 1
        if first + second == magic_num:
            print(f"Combination N:{counter} ({first} + {second} = {magic_num})")
            found = True
            break
    if found:
        break

if not found:
    print(f"{counter} combinations - neither equals {magic_num}")
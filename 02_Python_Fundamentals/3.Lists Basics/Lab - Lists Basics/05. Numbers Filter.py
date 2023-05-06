num = int(input())
list_even = []
list_odd = []
list_negative = []
list_positive = []

for i in range(num):
    number = int(input())
    if number % 2 == 0:
        list_even.append(number)
    else:
        list_odd.append(number)

    if number >= 0:
        list_positive.append(number)
    else:
        list_negative.append(number)

command = input()
if command == "even":
    print(list_even)
elif command == "odd":
    print(list_odd)
elif command == "negative":
    print(list_negative)
elif command == "positive":
    print(list_positive)

sum_leva = float(input())
num_coins = 0

sum_coins = int(sum_leva * 100)

while sum_coins > 0:
    if sum_coins - 200 >= 0:
        sum_coins -= 200
        num_coins += 1
    elif sum_coins - 100 >= 0:
        sum_coins -= 100
        num_coins += 1
    elif sum_coins - 50 >= 0:
        sum_coins -= 50
        num_coins += 1
    elif sum_coins - 20 >= 0:
        sum_coins -= 20
        num_coins += 1
    elif sum_coins - 10 >= 0:
        sum_coins -= 10
        num_coins += 1
    elif sum_coins - 5 >= 0:
        sum_coins -= 5
        num_coins += 1
    elif sum_coins - 2 >= 0:
        sum_coins -= 2
        num_coins += 1
    elif sum_coins - 1 >= 0:
        sum_coins -= 1
        num_coins += 1
print(num_coins)


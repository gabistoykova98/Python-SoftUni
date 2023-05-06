deposit_sum = float(input())
time = int(input())
percent = float(input())
percent_sum = percent / 100
sum = deposit_sum + time * ((deposit_sum * percent_sum) / 12)
print(sum)
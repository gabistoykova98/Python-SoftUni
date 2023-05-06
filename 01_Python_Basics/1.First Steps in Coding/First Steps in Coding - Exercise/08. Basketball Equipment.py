fee = int(input())
sneakers = fee - fee * 0.4
clothes = sneakers - sneakers * 0.2
ball = clothes / 4
accessories = ball / 5
total_price = fee + sneakers + clothes + ball + accessories
print(f"{total_price:.2f}")


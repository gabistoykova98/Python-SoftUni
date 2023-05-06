import math
magnolii = int(input())
zumbuli = int(input())
roses = int(input())
kaktusi = int(input())
present_price = float(input())
price = magnolii * 3.25 + zumbuli * 4.00 + roses * 3.50 + kaktusi * 8
tax = price * 0.05
total_price = price - tax
if total_price >= present_price:
    remainder = total_price - present_price
    print(f"She is left with {math.floor(remainder)} leva.")
else:
    need_money = abs(total_price - present_price)
    print(f"She will have to borrow {math.ceil(need_money)} leva.")
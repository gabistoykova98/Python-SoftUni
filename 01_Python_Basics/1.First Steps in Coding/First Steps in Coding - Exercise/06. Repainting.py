nylon = int(input())
paint = int(input())
thinner = int(input())
hours = int(input())
price = ((nylon + 2) * 1.50) + ((paint + (paint * 0.1)) * 14.50) + (thinner * 5.00) + 0.40
price_work = (price * 0.3) * hours
tottal_price = price + price_work
print(tottal_price)
pen = int(input())
marker = int(input())
cleaner = int(input())
percent = int(input())
price = pen * 5.80 + marker * 7.20 + cleaner * 1.20
discount = percent / 100
total_price = price - (price * discount)
print(total_price)
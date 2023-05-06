days = int(input())
type_of_room = input()
rating = input()
overnight_stay = days - 1
price = 0.00

if type_of_room == "room for one person":
    price = overnight_stay * 18.00
elif type_of_room == "apartment":
    if days < 10:
        price = (overnight_stay * 25.00) * 0.7
    elif 10 <= days <= 15:
        price = (overnight_stay * 25.00) * 0.65
    else:
        price = (overnight_stay * 25.00) * 0.5
elif type_of_room == "president apartment":
    if days < 10:
        price = (overnight_stay * 35.00) * 0.9
    elif 10 <= days <= 15:
        price = (overnight_stay * 35.00) * 0.85
    else:
        price = (overnight_stay * 35.00) * 0.8

if rating == "positive":
    price = price * 1.25
elif rating == "negative":
    price = price * 0.9

print(f'{price:.2f}')
budget = float(input())
season = input()
price = 0

if budget <= 100:
    if season =="summer":
        price += budget * 0.3
        print(f"Somewhere in Bulgaria")
        print(f"Camp - {price:.2f}")
    elif season == "winter":
        price += budget * 0.7
        print(f"Somewhere in Bulgaria")
        print(f"Hotel - {price:.2f}")
elif 100 <= budget <= 1000:
    if season == "summer":
        price += budget * 0.4
        print(f"Somewhere in Balkans")
        print(f"Camp - {price:.2f}")
    elif season == "winter":
        price += budget * 0.8
        print(f"Somewhere in Balkans")
        print(f"Hotel - {price:.2f}")
elif budget > 1000:
    if season == "summer" or season == "winter":
        price = budget * 0.9
        print(f"Somewhere in Europe")
        print(f"Hotel - {price:.2f}")
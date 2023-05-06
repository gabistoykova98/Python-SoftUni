month = input()
nights = int(input())

if month == "May" or month == "October":
    if nights <= 7:
        print(f"Apartment: {(nights * 65):.2f} lv.")
        print(f"Studio: {(nights * 50):.2f} lv.")
    elif 7 < nights <=14:
        print(f"Apartment: {(nights * 65):.2f} lv.")
        print(f"Studio: {(nights * 50 * 0.95):.2f} lv.")
    elif nights > 14:
        print(f"Apartment: {(nights * 65 * 0.9):.2f} lv.")
        print(f"Studio: {(nights * 50 * 0.7):.2f} lv.")
elif month == "June" or month == "September":
    if nights <= 14:
        print(f"Apartment: {(nights * 68.70):.2f} lv.")
        print(f"Studio: {(nights * 75.20):.2f} lv.")
    elif nights > 14:
        print(f"Apartment: {(nights * 68.70 * 0.9):.2f} lv.")
        print(f"Studio: {(nights * 75.20 * 0.8):.2f} lv.")
elif month == "July" or month == "August":
    if nights <= 14:
        print(f"Apartment: {(nights * 77):.2f} lv.")
        print(f"Studio: {(nights * 76):.2f} lv.")
    elif nights > 14:
        print(f"Apartment: {(nights * 77 * 0.9):.2f} lv.")
        print(f"Studio: {(nights * 76):.2f} lv.")



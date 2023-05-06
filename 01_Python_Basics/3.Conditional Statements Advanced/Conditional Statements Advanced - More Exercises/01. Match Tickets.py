budget = float(input())
ticket_type = input()
people = int(input())
transport = 0
sum_needed = 0
ticket = 0

if ticket_type == "Normal":
    ticket = 249.99
elif ticket_type == "VIP":
    ticket = 499.99

if 1 <= people <= 4:
    transport = budget * 0.75
elif 5 <= people <= 9:
    transport = budget * 0.6
elif 10 <= people <= 24:
    transport = budget * 0.5
elif 25 <= people <= 49:
    transport = budget * 0.4
elif people >= 50:
    transport = budget * 0.25

sum_ticket = ticket * people


if


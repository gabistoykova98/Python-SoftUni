town = input()

while town != "End":
    budget = float(input())
    total_money = 0
    while total_money < budget:
        money = float(input())
        total_money += money
    print(f"Going to {town}!")
    town = input()





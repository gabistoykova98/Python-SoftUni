import math

tournament = int(input())
start_points = int(input())
total_points = start_points
average_points = 0
win = 0

for i in range(1, tournament + 1):
    stage = input()
    if stage == "W":
        total_points += 2000
        average_points += 2000
        win += 1
    elif stage == "F":
        total_points += 1200
        average_points += 1200
    elif stage == "SF":
        total_points += 720
        average_points += 720

average_p = average_points / tournament
percent_won = win / tournament * 100

print(f"Final points: {total_points}")
print(f"Average points: {math.floor(average_p)}")
print(f"{percent_won:.2f}%")

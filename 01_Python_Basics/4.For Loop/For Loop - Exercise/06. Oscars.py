name_actor = input()
started_points = float(input())
number_judge = int(input())

total_points = started_points
for i in range(1, number_judge + 1):
    name_judge = input()
    points = float(input())
    current_points = (len(name_judge) * points) / 2
    total_points += current_points

    if total_points >= 1250.5:
        break

if total_points < 1250.5:
    diff = 1250.5 - total_points
    print(f"Sorry, {name_actor} you need {diff:.1f} more!")
else:
    print(f'Congratulations, {name_actor} got a nominee for leading role with {total_points:.1f}!')

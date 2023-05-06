string = [x for x in input().split()]
team_a = [int(x) for x in range(1, 12)]
team_b = [int(x) for x in range(1, 12)]
game_over = False

for i in range(len(string)):
    team, number = [int(x) if x.isdigit() else x for x in string[i].split("-")]
    if team == "A":
        if number in team_a:
            team_a.remove(number)
    elif team == "B":
        if number in team_b:
            team_b.remove(number)
    if len(team_a) < 7 or len(team_b) < 7:
        game_over = True
        break

print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
if game_over:
    print("Game was terminated")



free_days = int(input())
normal_play = 30000
free_days_play = free_days * 127
workdays = 365 - free_days
workdays_play = workdays * 63
playtime = free_days_play + workdays_play
total_play_time = abs(normal_play - playtime)
hours = total_play_time // 60
minutes = total_play_time % 60
if normal_play > playtime:
    print("Tom sleeps well")
    print(f"{hours} hours and {minutes} minutes less for play")
else:
    print("Tom will run away")
    print(f"{hours} hours and {minutes} minutes more for play")

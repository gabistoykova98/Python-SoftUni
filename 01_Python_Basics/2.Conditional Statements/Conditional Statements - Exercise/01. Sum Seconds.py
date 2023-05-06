time_first = int(input())
time_second = int(input())
time_third = int(input())
all_time = time_first + time_second + time_third
minutes = all_time // 60
seconds = all_time % 60
if seconds < 10:
    print(f"{minutes}:0{seconds}")
else:
    print(f"{minutes}:{seconds}")
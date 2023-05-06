import math
from math import ceil

serial = input()
serial_time = int(input())
lunch_break = int(input())

time_lunch = lunch_break / 8
time_relax = lunch_break / 4
free_time = lunch_break - time_relax - time_lunch
if free_time >= serial_time:
    excess = free_time - serial_time
    print(f"You have enough time to watch {serial} and left with {math.ceil(excess)} minutes free time.")
else:
    need_time = abs(free_time - serial_time)
    print(f"You don't have enough time to watch {serial}, you need {math.ceil(need_time)} more minutes.")

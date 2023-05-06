record_seconds = float(input())
meters = float(input())
time_sec_m = float(input())

time = meters * time_sec_m
slowdown = (meters // 15) * 12.5
all_time = time + slowdown

if all_time < record_seconds:
    print(f"Yes, he succeeded! The new world record is {all_time:.2f} seconds.")
else:
    time_more = all_time - record_seconds
    print(f"No, he failed! He was {time_more:.2f} seconds slower.")
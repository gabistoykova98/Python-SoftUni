pages = int(input())
pages_per_hour = int(input())
days = int(input())
hour_per_day = (pages // pages_per_hour) // days
print(hour_per_day)
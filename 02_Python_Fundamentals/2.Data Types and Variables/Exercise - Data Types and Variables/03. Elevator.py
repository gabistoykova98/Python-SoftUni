import math

num_people = int(input())
capacity = int(input())

if num_people / capacity <= 1:
    all_courses = math.ceil(num_people / capacity)
    print(all_courses)
elif num_people % capacity == 0:
    all_courses = math.floor(num_people // capacity)
    print(all_courses)
elif num_people % capacity > 0:
    all_courses = num_people // capacity
    print(f"{all_courses + 1}")



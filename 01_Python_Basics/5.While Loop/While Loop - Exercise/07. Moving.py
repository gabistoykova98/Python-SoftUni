width = int(input())
length = int(input())
height = int(input())
area = width * length * height
total_box = 0

command = input()
while command != "Done":
    num_box = int(command)
    total_box += num_box

    if total_box > area:
        print(f"No more free space! You need {abs(total_box - area)} Cubic meters more.")
        break

    command = input()

if area > total_box:
    print(f"{area - total_box} Cubic meters left.")


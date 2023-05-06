command = input()
all_coffee = 0

while command != "END":
    events = command
    if events == "coding" or events == "cat" or events == "dog" or events == "movie":
        all_coffee += 1
    elif events == "CODING" or events == "CAT" or events == "DOG" or events == "MOVIE":
        all_coffee += 2
    command = input()
if all_coffee > 5:
    print("You need extra sleep")
else:
    print(all_coffee)


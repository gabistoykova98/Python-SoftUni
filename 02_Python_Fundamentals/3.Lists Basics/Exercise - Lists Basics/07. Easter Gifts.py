receive_the_gifts = input().split()
END_COMMAND = "No Money"

commands = input()
while commands != END_COMMAND:
    type_of_command, *data = commands.split()

    if type_of_command == "OutOfStock":
        gift_name = data[0]
        for i in range(len(receive_the_gifts)):
            if gift_name in receive_the_gifts:
                if receive_the_gifts[i] == gift_name:
                    receive_the_gifts[i] = 'None'

    elif type_of_command == "Required":
        gift_name = data[0]
        index = int(data[1])
        if 0 <= index < len(receive_the_gifts):
            receive_the_gifts[index] = gift_name

    elif type_of_command == "JustInCase":
        name_gift = data[0]
        receive_the_gifts.pop()
        receive_the_gifts.append(name_gift)

    commands = input()

print(" ".join(x for x in receive_the_gifts if x != 'None'))
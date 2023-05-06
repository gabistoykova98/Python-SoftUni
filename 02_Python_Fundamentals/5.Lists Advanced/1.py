username = input()
command = input()
while command != "Registration":
    type_command, *info = command.split()
    if type_command == "Letters":
        if info[0] == "Lower":
            username = username.lower()
            print(username)
        elif info[0] == "Upper":
            username = username.upper()
            print(username)

    elif type_command == "Reverse":
        start_index = int(info[0])
        end_index = int(info[1])
        if 0 <= start_index < len(username) and 0 <= end_index < len(username):
            substring = username[start_index:end_index + 1]
            reversed_substring = substring[::-1]
            print(reversed_substring)

    elif type_command == "Substring":
        substring = str(info[0])
        if substring in username:
            username = username.replace(substring, "")
            print(username)
        else:
            print(f"The username {username} doesn't contain {substring}.")
    elif type_command == "Replace":
        char = info[0]
        username = username.replace(char, "-")
        print(username)
    elif type_command == "IsValid":
        char = info[0]
        if char in username:
            print("Valid username.")
        else:
            print(f"{char} must be contained in your username.")

    command = input()



command = input()

while command != "End":
    current_char = ""
    if command != "SoftUni":
        for char in command:
            print(char * 2, end="")

        print()
    command = input()


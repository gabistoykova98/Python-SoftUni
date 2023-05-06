import re

pattern = r'^U\$(?P<name>[A-Z][a-z]{3,})U\$P@\$(?P<pass>[A-Za-z]{5,}[0-9]{1,})P@\$'
counter = 0
count_input = int(input())
for i in range(count_input):
    strings = input()

    result = re.search(pattern, strings)

    if result:
        username = result.group('name')
        password = result.group('pass')
        counter += 1
        print(f"Registration was successful\n"
              f"Username: {username}, Password: {password}")

    else:
        print("Invalid username or password")
print(f"Successful registrations: {counter}")








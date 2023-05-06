num_of_strings = int(input())
for current_string in range(num_of_strings):
    word = input()
    if "," in word or "." in word or "_" in word:
        print(f"{word} is not pure!")
    else:
        print(f"{word} is pure.")
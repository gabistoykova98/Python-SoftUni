failed_grades = int(input())

last_example = ""
sum_grades = 0
count_examples = 0
poor_example = 0
fail = False

input_line = input()
while input_line != "Enough":
    current_grade = int(input())
    last_example = input_line

    if current_grade > 4:
        count_examples += 1
        sum_grades += current_grade
    elif current_grade <= 4:
        count_examples += 1
        poor_example += 1
        sum_grades += current_grade
        if poor_example >= failed_grades:
            fail = True
            break

    input_line = input()

average_sum = sum_grades / count_examples
if fail:
    print(f"You need a break, {poor_example} poor grades.")

else:
    print(f"Average score: {average_sum:.2f}")
    print(f"Number of problems: {count_examples}")
    print(f"Last problem: {last_example}")



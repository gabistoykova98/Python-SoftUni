
kid_ticket = 0
standard_ticket = 0
student_ticket = 0
movie_name = input()
total_tickets = 0

while movie_name != 'Finish':
    free_space = int(input())
    seats = 0

    for i in range(free_space):
        ticket = input()
        if ticket == "kid":
            kid_ticket += 1
        elif ticket == "student":
            standard_ticket += 1
        elif ticket == "standard":
            student_ticket += 1
        elif ticket == "End":
            break
        total_tickets += 1
        seats += 1

    movie_total_ticket = kid_ticket + student_ticket + standard_ticket
    print(f"{movie_name} - {(seats / free_space) * 100:.2f}% full.")

    movie_name = input()

print(f"Total tickets: {total_tickets}")
print(f"{student_ticket / total_tickets * 100:.2f}% student tickets.")
print(f"{standard_ticket / total_tickets* 100:.2f}% standard tickets.")
print(f"{kid_ticket /total_tickets * 100:.2f}% kids tickets.")

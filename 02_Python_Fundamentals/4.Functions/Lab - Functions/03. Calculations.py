name = input()
num_1 = int(input())
num_2 = int(input())


def calculate(name, num_1, num_2):
    result = 0
    if name == "multiply":
        result += num_1 * num_2
    elif name == "divide":
        result += num_1 // num_2
    elif name == "add":
        result += num_1 + num_2
    elif name == "subtract":
        result += num_1 - num_2
    return result


print(calculate(name, num_1, num_2))
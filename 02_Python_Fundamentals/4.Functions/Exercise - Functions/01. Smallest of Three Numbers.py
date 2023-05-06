def smallest(a, b, c):
    if a < b and a < c:
        # print(a) variant 1
        return a
    elif b < a and  b < c:
        return b
    elif c < b and c < a:
        return c



a = int(input())
b = int(input())
c = int(input())

print(smallest(a, b, c))
#mallest(a, b, c) variant 1

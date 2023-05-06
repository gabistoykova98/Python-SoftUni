def char(a, b):
    start = ord(a) + 1
    end = ord(b)
    listt = []
    for i in range(start, end):
        listt.append(chr(i))
    return " ".join(x for x in listt)
    # for x in listt:
    #     print(x, end=" ")

a = input()
b = input()

print(char(a, b))
# char(a, b)

# ord ot simvol kym cifra
# chr ot cifra kym simvol
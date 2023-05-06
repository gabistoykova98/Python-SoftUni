inp = list(map(int, input().split(", ")))
for ind in inp:
    if ind == 0:
        inp.remove(ind)
        inp.append(ind)

print(inp)




num = int(input())
word = input()
listt = []
list_two = []

for i in range(num):
    str = input()
    listt.append(str)
print(listt)

for g in range(len(listt)):
    if word in listt[g]:
        list_two.append(listt[g])
print(list_two)



x = [int(x) for x in input().split()]
listt = []

for i in x:
    if i % 2 == 0:
        listt.append(i)

print(listt)

# x = (int(x) for x in input().split())
# listt = []
# def even_(num):
#     if num % 2 == 0:
#         return True
#
# even_num = filter(even_, x)
#
# for x in even_num:
#     listt.append(x)
# print(listt)

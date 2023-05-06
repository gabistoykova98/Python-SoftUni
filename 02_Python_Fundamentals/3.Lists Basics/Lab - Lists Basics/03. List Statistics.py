number = int(input())
list_pos = []
list_neg = []

for i in range(number):
    num = int(input())
    if num >= 0:
        list_pos.append(num)
    else:
        list_neg.append(num)

print(list_pos)
print(list_neg)
print(f"Count of positives: {len(list_pos)}")
print(f"Sum of negatives: {sum(list_neg)}")




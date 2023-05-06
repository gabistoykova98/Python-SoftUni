nums = [int(num) for num in input().split(", ")]
count = int(input())
old_nums = []
new_nums = []
equal = False

for i in nums:
    old_nums.append(i)

while not equal:
    if len(old_nums) == count:
        equal = True

    elif len(old_nums) < count:
        old_nums.append(0)

    elif len(old_nums) > count:
        for z in range(0, count):
            new_nums.append(sum(old_nums[z::count]))
        break


if new_nums:
    print(new_nums)
elif equal:
    print(old_nums)



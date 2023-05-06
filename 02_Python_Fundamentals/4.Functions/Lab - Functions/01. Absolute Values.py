# inp = [float(x) for x in input().split()]
# result = [abs(x) for x in inp]
# print(result)

def abs_values(num):
    result = [abs(x) for x in num]
    return result


nums = [float(x) for x in input().split()]
print(abs_values(nums))
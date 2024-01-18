nums = [1,2,3,4]
n = len(nums)
res = [1] * n

prefix = 1
for i in range(1, n):
    prefix *= nums[i - 1]
    res[i] *= prefix
print(res)

postfix = 1
for i in range(len(nums)-1, -1, -1):
    res[i] *= postfix
    print(res[i])
    postfix *= nums[i]
print(res)
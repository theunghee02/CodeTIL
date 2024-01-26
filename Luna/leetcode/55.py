nums = [2,3,1,1,4]
idx = 0
for i in range(len(nums)-1):
    idx += nums[i]
    if idx == len(nums)-1: print(True)

print(False)
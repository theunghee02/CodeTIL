# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)-1):
#             for j in range(i+1, len(nums)):
#                 temp = nums[i] + nums[j]
#                 if temp == target:
#                     return [i,j]

nums = [3,2,4]
target = 6
num_dict = {}

for i, num in enumerate(nums):
    num_dict[num] = i

print(num_dict)
for i , num in enumerate(nums):
    res = target - num
    if res in num_dict and num_dict[res] != i:
        result = [i, num_dict[res]]

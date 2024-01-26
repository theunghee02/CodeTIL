from typing import List

class Solution:
    def maxSubArrayRecursively(self, nums: List[int], start, end):
        # base case
        if end - start == 0:
            return nums[end]

        # recursive case
        mid = (start + end) // 2
        leftMax = self.maxSubArrayRecursively(nums, start, mid)
        rightMax = self.maxSubArrayRecursively(nums, mid + 1, end)

        # Combine the results
        crossMax = self.maxCrossing(nums, start, mid, end)

        # Return the maximum of three
        return max(leftMax, rightMax, crossMax)

    def maxSubArray(self, nums: List[int]) -> int:
        print(self.maxSubArrayRecursively(nums, 0, len(nums) - 1))

    def maxCrossing(self, nums, start, mid, end):
        leftSum = float('-inf')
        currSum = 0
        for i in range(mid, start - 1, -1):
            currSum += nums[i]
            leftSum = max(leftSum, currSum)

        rightSum = float('-inf')
        currSum = 0
        for i in range(mid + 1, end + 1):
            currSum += nums[i]
            rightSum = max(rightSum, currSum)
        print(leftSum + rightSum)
        return leftSum + rightSum

nums = [5,4,-1,7,8]
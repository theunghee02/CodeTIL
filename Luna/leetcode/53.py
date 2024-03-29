class Solution(object):
    def maxSubArray(self, nums):
        n = len(nums)
        start = [0] * n  # 각 위치에서 시작하는 부분 배열의 최대 합을 저장하는 배열
        max_sum = [0] * n  # 각 위치에서의 최대 부분 배열의 합을 저장하는 배열

        # 배열의 마지막 값으로 초기화
        start[n - 1] = max_sum[n - 1] = nums[n - 1]

        # 배열 끝에서부터 시작하여 각 위치에서의 최대 부분 배열의 합 계산
        for i in range(n - 2, -1, -1):
            if start[i + 1] > 0:
                start[i] = nums[i] + start[i + 1]
            else:
                start[i] = nums[i]

            max_sum[i] = max(max_sum[i + 1], start[i])
        return max_sum[0]

# Example usage:
solution = Solution()
nums = [5,4,-1,7,8]
result = solution.maxSubArray(nums)
print(result)

#sol2)
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
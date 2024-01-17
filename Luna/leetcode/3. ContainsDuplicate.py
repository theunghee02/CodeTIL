class Solution(object):
    def containsDuplicate(self, nums):
        # 중복이 있는지 없는지 확인하기 위해 집합을 하나 만듬
        nums_cnt = set()
        for num in nums:
            if num in nums_cnt:
                return True
            nums_cnt.add(num)
        return False


def canJump(nums):
    max_reach = 0

    for i in range(len(nums)):
        # 현재 위치에서 최대로 갈 수 있는 거리 업데이트
        max_reach = max(max_reach, i + nums[i])
        print(max_reach)
        # 만약 현재 위치가 최대 도달 거리를 벗어나면 종료
        if max_reach < i + 1 and i < len(nums) - 1:
            return False

    return True

nums = [3,2,1,0,4]
print(canJump(nums))
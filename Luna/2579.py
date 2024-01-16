N = int(input())
stairs = [0] * (N+1)
dp = [[0 for _ in range(3)] for _ in range(N+1)]
for i in range(1, N+1):
    stairs[i] = int(input())

## 도착점일때 부터 고려하는 풀이 - 첫번째 부터 시작하면 여러 경우가 나뉘기 때문에 뒤에서 푸는게 좋음
def func(stairs, i, cnt):
    # 출발점 == 도착점일때
    if i == len(stairs):
        return stairs[i]
    elif dp[i][cnt] != 0:
        return dp[i][cnt]
    
    ret = 0
    # 나까지 오는데 이미 2번 연속 했다면, 한칸 밖에 뛰지 못함
    if cnt == 2:
        ret = func(stairs, i+2, 1)
    # 두번 연속하지 않았더라면, 한칸 뛰기 OR 두칸 뛰기
    else:
        ret = max(func(stairs, i+2, 1), func(stairs, i+1, cnt+1)) + stairs[i]

    dp[i][cnt] = ret
    return dp[i][cnt]

print(func(stairs, 1, 1))
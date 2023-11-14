def sol(n):
    if n == 1: return 1
    if n == 2: return 2
    # 이미 계산된 적이 있다면
    if dp[n] != 0:
        return dp[n]
    ## 계산되지 않았다면, 저장
    dp[n] = (sol(n-1) + sol(n-2)) %15746
    return dp[n]

N = int(input())
dp = [0] * (N+1)
print(sol(N)%15746)
def sol(n):
    if n == 1: return 1
    if n == 2: return 2
    dp[n] = sol(n-1) + sol(n-2)
    return dp[n]

N = int(input())
dp = [0] * (N+1)
print(sol(N)%15746)
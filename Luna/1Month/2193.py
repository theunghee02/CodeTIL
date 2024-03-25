N = int(input())
# N = 자릿수
dp = [[-1 for _ in range(91)] for _ in range(2)]

dp[0][1] = 1 #0 으로 시작하는 한자리수 - 1개
dp[1][1] = 1 # 1로 시작하는 한 자리수 - 1개

for i in range(2, N+1):
    dp[1][i] = dp[0][i-1]
    dp[0][i] = dp[0][i-1] + dp[1][i-1]
print(dp[1][N])

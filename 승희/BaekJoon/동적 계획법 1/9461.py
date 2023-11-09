import sys
n = int(sys.stdin.readline().rstrip())
dp = [0] * 101
dp[1], dp[2], dp[3] = 1, 1, 1

for i in range(n) :
    ni = int(sys.stdin.readline().rstrip())
    for j in range(4, ni+1) :
        dp[j] = dp[j-3] + dp[j-2]
    print(dp[ni])
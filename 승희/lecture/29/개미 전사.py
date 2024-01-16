import sys
n = int(sys.stdin.readline().rstrip())
ks = list(map(int, sys.stdin.readline().rstrip().split()))
dp = [0] * n

# dp의 0,1 위치를 초기화 하는 이유: n이 3 이상이기 때문
dp[0] = ks[0]
dp[1] = max(ks[0], ks[1])
for i in range(2,n):
    dp[i] = max(dp[i-1], dp[i-2]+ks[i])

# print(max(dp))
print(dp[n-1])
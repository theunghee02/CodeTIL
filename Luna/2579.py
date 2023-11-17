N = int(input())
stairs = [0] * (N+1)
for i in range(N):
    stairs[i] = int(input())
dp = [0] * N
dp[0] = stairs[0]
dp[1] = stairs[0] + stairs[1]
dp[2] = max(stairs[1] + stairs[2], stairs[0] + stairs[2])

for i in range(3, N):
    dp[i] = max()
print(stairs)
N = int(input())
# N = 자릿수, 0~9까지의 숫자(시작하는 수)
dp = [[-1 for _ in range(10)]for i in range(N+1)]
# row = 길이
# col = 시작하는 숫자

# BaseCase : 길이가 1
for i in range(10):
    dp[1][i] = 1 #길이는 1개는 하나만 온다.

for i in range(2, N+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][1]
        elif j == 9:
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
sum = 0
for i in range(1, 10):
    sum += dp[N][i]
print(sum%1000000000)
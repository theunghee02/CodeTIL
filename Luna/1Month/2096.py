N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
max_dp = [[0 for _ in range(N)] for _ in range(N)]
min_dp = [[0 for _ in range(N)] for _ in range(N)]

max_dp[0] = arr[0] # 1행 초기화
min_dp[0] = arr[0]

for i in range(1,N):
    for j in range(N):
        if j == 0:
            max_dp[i][j] = arr[i][j] + max(max_dp[i - 1][j], max_dp[i - 1][j + 1])
            min_dp[i][j] = arr[i][j] + min(min_dp[i - 1][j], min_dp[i - 1][j + 1])
        elif j == N - 1:
            max_dp[i][j] = arr[i][j] + max(max_dp[i - 1][j], max_dp[i - 1][j - 1])
            min_dp[i][j] = arr[i][j] + min(min_dp[i - 1][j], min_dp[i - 1][j - 1])

        else:
            max_dp[i][j] = arr[i][j] + max(max_dp[i - 1][j], max_dp[i - 1][j - 1], max_dp[i - 1][j + 1])
            min_dp[i][j] = arr[i][j] + min(min_dp[i - 1][j], min_dp[i - 1][j - 1], min_dp[i - 1][j + 1])

        # 마지막 행에서 최대값과 최소값 출력
print(max(max_dp[N - 1]), min(min_dp[N - 1]))
## 이친수
# 1. 1로 시작
# 2. 두번 연속으로 1 아님
def function(N, start, dp):
# 한자리수 일때
    if N == 1 :
        return 1
    if N == 2 :
        if start == 1: return 1
        elif start == 0: return 2
    if dp[start][N] != -1:
        return dp[start][N]

    if start == 0:
        dp[start][N] = function(N-1, 0, dp) + function(N-1, 1, dp)
    elif start == 1: #1로 시작하는 것은 뒤에 무조건 0밖에..
        dp[start][N] = function(N-1, 0, dp)
    return dp[start][N]

N = int(input())
# N = 자릿수
# y = 시작하는 수
dp = [[-1 for _ in range(91)] for i in range(2)]
print(function(N, 1, dp))
# def sol(n):
#     ## 1자리 일때 1
#     if n == 1: return 1
#     ## 2자리 일때 00,11 
#     if n == 2: return 2
#     # 이미 계산된 적이 있다면
#     if dp[n] != 0:
#         return dp[n]
#     ## 계산되지 않았다면, 저장
#     else : 
#         dp[n] = (sol(n+1) + sol(n+2)) %15746
#         return dp[n]
import sys
input = sys.stdin.readline
n= int(input())
dp = [0] * 1000001
dp[1] = 1
dp[2] = 2

for i in range(3, n+1):
    dp[i]= (dp[i-1] + dp[i-2])%15746
print(dp[n])
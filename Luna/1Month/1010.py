# ## 풀이방법 정리
# #1. 이전 sight에서 고른 오른쪽 sight를 m이라고 하자
# #2. 오른쪽 sight에서 m+1 ~ 마지막까지 하나 고르고
# #3. 나머지는 재귀함수로 넘김
# ## 재귀함수는 내가 할일만 잘 정의하면 된다...!!
#
# # n =서 , m = 동
def bridge_count(n, m, dp):
    if n == m:
        dp[n][m] = 1
        return 1
    if n == 1:
        dp[n][m] = m
    if dp[n][m] != -1:
        return dp[n][m]
    dp[n][m] = bridge_count(n, m-1, dp) + bridge_count(n-1, m-1, dp)
    return dp[n][m]
T = int(input())
for i in range(T):
    a, b = map(int, input().split())
    dp = [[-1 for _ in range(b+1)]for _ in range(a + 1)]
    print(bridge_count(a, b, dp))
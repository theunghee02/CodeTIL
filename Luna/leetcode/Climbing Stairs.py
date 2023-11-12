
def climbStairs(n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1: return 1
        if n == 2: return 2
        dp[n] = climbStairs(n-1) + climbStairs(n-2)
        return dp[n]
       
n = int(input())
dp = [0]*(n+1)
print(climbStairs(n))

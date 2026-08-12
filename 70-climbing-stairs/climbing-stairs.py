class Solution(object):
    def climbStairs(self, n):
        # memo=[-1]*(n+1)
        # def backtrack(n):
        #     if n<=2:
        #         return n
        #     if memo[n]!=-1:
        #         return memo[n]
        #     memo[n]=backtrack(n-1)+backtrack(n-2)
        #     return memo[n]
        # return backtrack(n)
        if n<=2:
            return n
        dp = [0]*n
        dp[0] = 1
        dp[1] = 2
        for i in range(2,n):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]
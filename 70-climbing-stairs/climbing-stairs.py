class Solution:
    def climbStairs(self, n: int) -> int:
        def memoization(n):
            if n<=2:
                return n
            if memo[n]!=-1:
                return memo[n]
            memo[n]=memoization(n-1)+memoization(n-2)
            return memo[n]
        memo=[-1]*(n+1)
        return memoization(n)
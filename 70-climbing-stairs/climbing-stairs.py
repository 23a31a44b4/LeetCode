class Solution(object):
    def climbStairs(self, n):
        memo=[-1]*(n+1)
        def backtrack(n):
            if n<=2:
                return n
            if memo[n]!=-1:
                return memo[n]
            memo[n]=backtrack(n-1)+backtrack(n-2)
            return memo[n]
        return backtrack(n)
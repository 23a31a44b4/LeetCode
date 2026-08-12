class Solution(object):
    def fib(self, n):
        # def fib(n):
        #     if n<2:
        #         return n
        #     return fib(n-1)+fib(n-2)
        # return fib(n)

        #memo
        # memo = [-1]*(n+1)
        # def memoization(n):
        #     if n<2:
        #         return n
        #     if memo[n]!=-1:
        #         return memo[n]
        #     memo[n] = memoization(n-1)+memoization(n-2)
        #     return memo[n]
        # memoization(n)
        # return memo[-1]      

        #tabulation
        # if n<2:
        #     return n
        # dp = [0]*(n+1)
        # dp[1] = 1
        # for i in range(2,n+1):
        #     dp[i]=dp[i-1]+dp[i-2]
        # return dp[-1]  

        #spaceoptimization
        if n<2:
            return n
        f0 = 0
        f1 = 1
        for _ in range(2,n+1):
            res = f0 + f1
            f0 = f1
            f1 = res
        return f1
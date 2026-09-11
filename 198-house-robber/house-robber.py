class Solution:
    def rob(self, nums: List[int]) -> int:
        r1=0
        r2=0
        for i in range(len(nums)-1,-1,-1):
            r=max(nums[i]+r2,r1)
            r2=r1
            r1=r
        return r1
        # def backtrack(n):
        #     if n>=len(nums):
        #         return 0
        #     return max(nums[n]+backtrack(n+2),backtrack(n+1))
        # return backtrack(0)

        # def memoization(n):
        #     if n>=len(nums):
        #         return 0
        #     if memo[n]!=-1:
        #         return memo[n]
        #     memo[n]=max(nums[n]+memoization(n+2),memoization(n+1))
        #     return memo[n]
        # memo=[-1]*len(nums)
        # return memoization(0)

        # dp=[-1]*len(nums)+[0,0]
        # for i in range(len(nums)-1,-1,-1):
        #     dp[i]=max(nums[i]+dp[i+2],dp[i+1])
        # return dp[0]
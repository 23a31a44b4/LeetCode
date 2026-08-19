class Solution(object):
    def maxSubArray(self, nums):
        cur_sum=0
        ans=nums[0]
        for num in nums:
            if cur_sum<0:
                cur_sum=0
            cur_sum+=num
            ans= max(cur_sum,ans)
        return ans

        
        
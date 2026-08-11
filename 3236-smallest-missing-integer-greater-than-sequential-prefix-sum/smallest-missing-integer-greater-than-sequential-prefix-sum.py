class Solution(object):
    def missingInteger(self, nums):
        ans=nums[0]
        dup=set(nums)
        for j in range(1,len(nums)):
            if nums[j]==nums[j-1]+1:
                ans+=nums[j]
            else:
                break
        while ans in dup:
            ans+=1
        return ans
        
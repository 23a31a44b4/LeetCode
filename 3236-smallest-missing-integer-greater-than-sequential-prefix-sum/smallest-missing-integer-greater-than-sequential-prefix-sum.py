class Solution(object):
    def missingInteger(self, nums):
        i=0
        seen=set(nums)
        ans=nums[0]
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]+1:
                ans+=nums[i]
            else:
                break
        while ans in seen:
            ans+=1

        return ans
        

        
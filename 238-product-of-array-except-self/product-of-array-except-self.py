class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans=1
        res=[0]*len(nums)
        zero=nums.count(0)
        if zero>1:
            return res
        for i in nums:
            if i!=0:
                ans=ans*i
        if zero==1:
            zero_idx=nums.index(0)
            res[zero_idx]=ans
            return res
        for i,x in enumerate(nums):
            res[i]=ans//x
        return res

        
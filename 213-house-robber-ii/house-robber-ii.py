class Solution(object):
    def rob(self, nums):
        if len(nums)<=1:
            return nums[0]
        r1,r2=0,0
        n=len(nums)
        nums1=nums[:n-1]
        for i in range(len(nums1)):
            res=max(nums1[i]+r1,r2)
            r1=r2
            r2=res
        nums2=nums[1:]
        r3,r4=0,0
        for i in range(len(nums2)):
            res=max(nums2[i]+r3,r4)
            r3=r4
            r4=res     
        return max(r2,r4)
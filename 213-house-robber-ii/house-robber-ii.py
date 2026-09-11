class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        n=len(nums)
        nums1=nums[:n-1]
        nums2=nums[1:]
        dp1=nums1+[0,0]
        dp2=nums2+[0,0]
        for i in range(len(nums1)-1,-1,-1):
            dp1[i]=max(nums1[i]+dp1[i+2],dp1[i+1])
            dp2[i]=max(nums2[i]+dp2[i+2],dp2[i+1])
        return max(dp1[0],dp2[0])
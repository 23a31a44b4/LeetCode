class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l=k=0
        r=len(nums)-1
        while k<=r:
            if nums[k]==0:
                nums[k],nums[l]=nums[l],nums[k]
                l+=1
                k+=1
            elif nums[k]==2:
                nums[k],nums[r]=nums[r],nums[k]
                r-=1
            else:
                k+=1
        return nums
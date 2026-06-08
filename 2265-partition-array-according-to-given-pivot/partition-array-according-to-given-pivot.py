class Solution(object):
    def pivotArray(self, nums, pivot):
        n=len(nums)
        pivota=[]
        left=[]
        right=[]
        for i in range(0,n):
            if nums[i]==pivot:
                pivota.append(nums[i])
            elif nums[i]>pivot:
                right.append(nums[i])
            elif nums[i]<pivot:
                left.append(nums[i])
        return left+pivota+right
        
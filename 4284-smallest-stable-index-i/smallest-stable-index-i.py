class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        def high(arr):
            arr.sort()
            return arr[-1]
        def small(srr):
            srr.sort()
            return srr[0]
        x=float('inf')
        for i,num in enumerate(nums):
            score=high(nums[:i+1])-small(nums[i:])
            if score<=k:
                return i
        return -1
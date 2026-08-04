class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        heap_set=set(nums)
        res=[]
        small=min(nums)
        high=max(nums)
        for i in range(small+1,high):
            if i not in heap_set:
                res.append(i)
        return res


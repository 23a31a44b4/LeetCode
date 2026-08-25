class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        seen=set(nums)
        i=1
        while True:
            if k*i in seen:
                i+=1
            else:
                return k*i
                breaak
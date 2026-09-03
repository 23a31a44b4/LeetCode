class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        odd=float('inf')
        for num in nums1:
            if num%2!=0:
                odd=min(odd,num)
        if odd==float('inf'):
            return True
        
        for num in nums1:
            if num%2==0 and num<=odd:
                return False
        return True
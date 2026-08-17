class Solution(object):
    def missingNumber(self, nums):
        n=len(nums)
        if n>1:
            hash_map=[-1]*(n+1)
            for i in nums:
                hash_map[i]=i
            for i in range(n+1):
                if hash_map[i] == -1:
                    return i
        else:
            if nums[0]==0:
                return 1
            else:
                return 0

        
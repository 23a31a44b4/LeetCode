class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cur_sum=maxsum=sum(nums[:k])
        for i in range(k,len(nums)):
            cur_sum+=nums[i]-nums[i-k]
            maxsum=max(maxsum,cur_sum)
        return maxsum/k
        
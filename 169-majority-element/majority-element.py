class Solution(object):
    def majorityElement(self, nums):
        candidate=nums[0]
        count=1
        for i in nums[1:]:
            if i==candidate:
                count+=1
            elif i!=candidate:
                if count==0:
                    candidate=i
                else:
                    count-=1
        return candidate
        
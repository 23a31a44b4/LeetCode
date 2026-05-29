class Solution(object):
    def minElement(self, nums):
        l=[]
        for i in nums:
            s=str(i)
            digit_sum=sum(int(digit) for digit in s)
            l.append(digit_sum)
        return min(l)
        
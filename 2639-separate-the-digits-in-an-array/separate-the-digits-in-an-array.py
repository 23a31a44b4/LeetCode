class Solution(object):
    def separateDigits(self, nums):
        ans=[]
        a=str(nums)
        for i in a:
            if i not in ['[',']',',',' ']:
                ans.append(int(i))
        return ans
        
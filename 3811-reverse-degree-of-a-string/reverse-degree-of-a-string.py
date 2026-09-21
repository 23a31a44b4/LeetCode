class Solution(object):
    def reverseDegree(self, s):
        ans=0
        for idx,ch in enumerate(s):
            degree=ord('z')-ord(ch)+1
            ans+=(degree*(idx+1))
        return ans
        
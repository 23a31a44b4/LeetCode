class Solution(object):
    def mirrorDistance(self, n):
        reverse=int(str(n)[::-1])
        ans=abs(reverse-n)
        return ans
        
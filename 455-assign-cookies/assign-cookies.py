class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(reverse=True)
        s.sort(reverse=True)
        j=0
        res=0
        for i in range(len(g)):
            if j>=len(s):
                break
            if s[j]>=g[i]:
                j+=1
                res+=1
        return res
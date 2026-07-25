class Solution:
    def maxProduct(self, n: int) -> int:
        n=str(n)
        ans=0
        f=0
        for f in range(len(n)):
            for s in range(f+1,len(n)):
                if ans<=int(n[f])*int(n[s]):
                    ans=int(n[f])*int(n[s])
        return ans
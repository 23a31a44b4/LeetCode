class Solution:
    def maxScore(self, cd: List[int], k: int) -> int:
        i=0
        e=len(cd)-k
        temp=sum(cd[e:])
        res=temp
        for j in range(e,len(cd)):
            temp-=cd[j]
            temp+=cd[i]
            i+=1
            res=max(temp,res)
        return res
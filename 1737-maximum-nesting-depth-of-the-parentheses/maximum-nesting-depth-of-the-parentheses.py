class Solution:
    def maxDepth(self, s: str) -> int:
        graph={}
        count=0
        ans=0
        for ch in s:
            if ch=='(':
                count+=1
            # if ch.isdigit():
            #     graph[int(ch)]=count
            if ch==')':
                ans=max(ans,count)
                count-=1
        return ans
            
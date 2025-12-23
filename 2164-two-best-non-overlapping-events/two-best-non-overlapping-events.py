import heapq
class Solution(object):
    def maxTwoEvents(self, events):
        events.sort()
        ans=0
        pq=[]
        max_far=0
        for start,end,value in events:
            while pq and pq[0][0]<start:
                i,j=heapq.heappop(pq)
                max_far=max(max_far,j)
            ans=max(ans,max_far+value)
            heapq.heappush(pq,(end,value))
        return ans
        
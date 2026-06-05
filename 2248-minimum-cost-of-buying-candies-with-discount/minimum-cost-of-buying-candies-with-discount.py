class Solution(object):
    def minimumCost(self, cost):
        cost.sort()
        ans=0
        count=0
        for i in range(len(cost)-1,-1,-1):
            if count==2:
                count=0
                continue
            count+=1
            ans+=cost[i]
        return ans
        
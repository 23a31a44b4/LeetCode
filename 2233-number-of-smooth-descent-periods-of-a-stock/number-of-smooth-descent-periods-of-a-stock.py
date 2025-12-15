class Solution(object):
    def getDescentPeriods(self, prices):
        n=len(prices)
        count=1
        ans=1
        for i in range(1,n):
            if prices[i-1]-prices[i]==1:
                count+=1
            else:
                count=1
            ans=ans+count
        return ans




        
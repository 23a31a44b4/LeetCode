class Solution(object):
    def maxIceCream(self, costs, coins):
        costs.sort()
        count=0
        val=0
        for i in costs:
            if val+i<=coins:
                val=val+i
                count+=1
        return count
        
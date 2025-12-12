#leetcode 11
class Solution(object):
    def maxArea(self, height):
       l=0
       r=len(height)-1
       cap=0
       while l<r:
        if height[l]>height[r]:
            if cap<(r-l)*(height[r]):
                cap=(r-l)*(height[r])
            r-=1
        else:
            if cap<(r-l)*(height[l]):
                cap=(r-l)*(height[l])
            l+=1
       return cap
            
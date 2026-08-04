class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,res=0,0
        r=len(height)-1
        while l!=r:
            cap=min(height[l],height[r])*(r-l)
            res=max(cap,res)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return res

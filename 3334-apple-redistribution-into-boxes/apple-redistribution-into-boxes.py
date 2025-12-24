class Solution(object):
    def minimumBoxes(self, apple, capacity):
        n=len(capacity)
        r=n-1
        boxes=0
        capacity.sort()
        apple_sum=sum(apple)
        while apple_sum>0 and r>=0:
            apple_sum-=capacity[r]
            r-=1
            boxes+=1
        return boxes
        
class Solution(object):
    def productExceptSelf(self, nums):
        ans=1
        zero=0
        for num in nums:
            if num==0:
                zero+=1
            else:
                ans*=num
        print(ans)
        
        if zero==0:
            res=[]
            for num in nums:
                res.append(ans//num)
            
        elif zero==1:
            res=[]
            for num in nums:
                if num==0:
                    res.append(ans)
                else:
                    res.append(0)
        elif zero>=2:
            res=[0]*len(nums)
        return res

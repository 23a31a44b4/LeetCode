class Solution(object):
    def largestInteger(self, nums, k):
        if k==1:
            hash_map={}
            for num in nums:
                hash_map[num]=hash_map.get(num,0)+1
            ans=-1
            for num,count in hash_map.items():
                if count==1:
                    if ans<num:
                        ans=num
            return  ans
        if k==len(nums):
            return max(nums)
        
        hash_map={}
        l=0
        r=k-1
        while r<len(nums):
            for i in range(l,r+1):
                hash_map[nums[i]]=hash_map.get(nums[i],0)+1
            l+=1
            r+=1
        ans=-1
        for k,v in hash_map.items():
            if v==1:
                if ans<k:
                    ans=k
        print(hash_map)
        return ans
        
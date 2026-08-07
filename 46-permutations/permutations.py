class Solution(object):
    def permute(self, nums):
        res = []
        def b (nums,path):
            if nums == []:
                res.append(path)
                return
            for i in range(len(nums)):
                b(nums[:i]+nums[i+1:],path+[(nums[i])])
        b(nums,[])
        return res
        
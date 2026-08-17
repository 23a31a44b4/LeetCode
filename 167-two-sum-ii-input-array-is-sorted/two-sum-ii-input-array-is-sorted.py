class Solution(object):
    def twoSum(self, numbers, target):
        # hash_map={}
        # for i in range(len(numbers)):
        #     if  numbers[i] in hash_map:
        #         return [hash_map[numbers[i]]+1,i+1]
        #     hash_map[target-numbers[i]]=i

        l=0
        r=len(numbers)-1
        while l<r:
            mid=numbers[l]+numbers[r]
            if target==mid:
                return [l+1,r+1]
            elif target<=mid:
                r-=1
            else:
                l+=1
        
        
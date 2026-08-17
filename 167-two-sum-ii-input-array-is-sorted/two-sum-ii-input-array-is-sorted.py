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
            if target==numbers[l]+numbers[r]:
                return [l+1,r+1]
            elif target<=numbers[l]+numbers[r]:
                r-=1
            else:
                l+=1
        
        
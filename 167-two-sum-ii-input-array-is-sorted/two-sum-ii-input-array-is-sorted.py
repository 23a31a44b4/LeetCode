class Solution(object):
    def twoSum(self, numbers, target):
        hash_map={}
        for i in range(len(numbers)):
            if  numbers[i] in hash_map:
                return [hash_map[numbers[i]]+1,i+1]
            hash_map[target-numbers[i]]=i
        
        
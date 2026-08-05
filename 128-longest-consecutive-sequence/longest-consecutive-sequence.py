class Solution(object):
    def longestConsecutive(self, nums):
        long=0
        hash_map={}
        for num in nums:
            hash_map[num]=hash_map.get(num,0)+1
        for num in hash_map:
            if num-1 not in hash_map:
                cur_num=num
                current=1
                while cur_num+1 in hash_map:
                    cur_num+=1
                    current+=1
                long=max(long,current)
        return long
        
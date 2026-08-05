from itertools import islice
class Solution(object):
    def topKFrequent(self, nums, k):
        hash_map={}
        ans=[]
        for num in nums:
            hash_map[num]=hash_map.get(num,0)+1
        sorted_items=(sorted(hash_map.items(), key=lambda item: item[1],reverse=True))
        return [item[0] for item in sorted_items[:k]]
        
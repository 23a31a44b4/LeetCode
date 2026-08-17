class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        hash_map={}
        for i in range(len(nums)):
            if nums[i] in hash_map:
                if i-hash_map[nums[i]]<=k:
                    return True
            hash_map[nums[i]]=i
        return False

class Solution(object):
    def intersection(self, nums1, nums2):
        hash_map1={}
        hash_map2={}
        ans=[]
        for num in nums1:
            hash_map1[num]=hash_map1.get(num,0)+1
        for num in nums2:
            hash_map2[num]=hash_map2.get(num,0)+1
        for num in hash_map1:
            if num in hash_map2:
                ans.append(num)
        return ans

        
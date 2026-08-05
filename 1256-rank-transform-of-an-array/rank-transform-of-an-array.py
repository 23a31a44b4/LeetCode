class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        arr1=sorted(arr)
        n=len(arr)
        hash_map={}
        rank=1
        for i in range(n):
            if arr1[i] not in hash_map:
                hash_map[arr1[i]]=rank
                rank+=1
        for i in range(n):
            arr[i]=hash_map[arr[i]]
        return arr

            
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map={}
        for ch in strs:
            res="".join(sorted(ch))
            if res in hash_map:
                hash_map[res].append(ch)
            else:
                hash_map[res]=[ch]
        print(hash_map)
        ans=[]
        for k,v in hash_map.items():
            ans.append(v)
        return ans
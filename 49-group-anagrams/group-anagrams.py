class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        for ch in strs:
            temp="".join(sorted(ch))
            if temp in hash_map:
                hash_map[temp].append(ch)
            else:
                hash_map[temp]= [ch]
        return list(hash_map.values())
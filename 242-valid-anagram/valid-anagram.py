class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        heap_map_s={}
        heap_map_t={}
        for i in range(len(s)):
            heap_map_s[s[i]]=heap_map_s.get(s[i],0)+1
            heap_map_t[t[i]]=heap_map_t.get(t[i],0)+1
        return heap_map_s==heap_map_t
class Solution:
    def compress(self, chars: List[str]) -> int:
        # hash_map={}
        # for ch in chars:
        #     hash_map[ch]=hash_map.get(ch,0)+1
        # res=[]
        # for k,v in hash_map.items():
        #     res.append(k)
        #     if v!=1:
        #         for digit in str(v):
        #             res.append(digit)
                
        # chars[:]=res
        # return len(chars)
        s=''
        n=len(chars)
        i=0
        while i<n:
            count=1
            while i+1<n and chars[i]==chars[i+1]:
                count+=1
                i+=1
            s+=chars[i]
            if count>1:
                s+=str(count)
            i+=1
        c_len=len(s)
        for j in range(c_len):
            chars[j]=s[j]
        del chars[c_len:]
        return len(s)
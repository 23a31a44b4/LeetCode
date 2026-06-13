class Solution(object):
    def mapWordWeights(self, words, weights):
        s=''
        for word in words:
            count=0
            for ch in word:
                idx=ord(ch)-ord('a')
                count+=weights[idx]
            print(count)
            char_idx=count%26
            s+=chr(ord('z')-char_idx)
        return s
        
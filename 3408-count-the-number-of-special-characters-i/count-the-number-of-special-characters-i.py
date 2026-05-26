class Solution(object):
    def numberOfSpecialChars(self, word):
        a=set()
        for ch in word:
            if ch.lower() not in a and ch.upper() in word and ch.lower() in word:
                a.add(ch.lower())
        return len(a)
        
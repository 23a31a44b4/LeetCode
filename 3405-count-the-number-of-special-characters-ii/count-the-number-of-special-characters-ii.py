class Solution(object):
    def numberOfSpecialChars(self, word):
        count=0
        for ch in 'abcdefghijklmnopqrstuvwxyz':
            lower=ch
            upper=ch.upper()

            if lower in word and upper in word:
                if word.rfind(lower)<word.find(upper):
                    count+=1
        return count
        
class Solution(object):
    def totalWaviness(self, num1, num2):
        def wavi(n):
            if n<100:
                return False
            s=str(n)
            peak=0
            valley=0
            for i in range(1,len(s)-1):
                if s[i]>s[i-1] and s[i]>s[i+1]:
                    peak+=1
                if s[i]<s[i-1] and s[i]<s[i+1]:
                    valley+=1
            return peak+valley

        ans=0
        for i in range(num1,num2+1):
            ans+=wavi(i)
        return ans
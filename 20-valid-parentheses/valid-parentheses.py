class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        # if s[0]==')' or s[0]==']' or s[0]=='}':
        #     return False
        for ch in s:
            if ch=='(' or ch=='[' or ch =='{':
                stack.append(ch)
                continue
            elif ch ==')':
                if stack and stack[-1]=='(':
                    stack.pop()
                else:
                    stack.append(ch)
            elif ch == ']':
                if stack and stack[-1]=='[':
                    stack.pop()
                else:
                    stack.append(ch)
            elif ch =='}' :
                if stack and stack[-1]=='{':
                    stack.pop()
                else:
                    stack.append(ch)
        return len(stack)==0
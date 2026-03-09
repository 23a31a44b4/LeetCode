class Solution(object):
    def isValid(self, s):
        stack=[]
        for ch in s:
            if ch=='(':
                stack.append(')')
            elif ch=='[':
                stack.append(']')
            elif ch=='{':
                stack.append('}')
            elif not stack or ch!=stack.pop():
                return False
        return not stack
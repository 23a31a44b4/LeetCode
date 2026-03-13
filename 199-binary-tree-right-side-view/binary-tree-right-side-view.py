# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        if not root:
            return []
        res=[]
        queue=[root]
        while queue:
            sublist=[]
            for _ in range(len(queue)):
                cur = queue.pop(0)
                sublist.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            res.append(sublist[-1])
            
        return res
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        node=[]
        global sum,count
        sum=0
        count=0
        def preorder(root):
            if root is None:
                return 0,0
            leftsum,leftcount=preorder(root.left)
            rightsum,rightcount=preorder(root.right)
            return leftsum+rightsum+root.val,leftcount+rightcount+1
        stack=[root]
        while stack:
            current=stack.pop()
            totalsum,totalcount=preorder(current)
            node.append([current.val,totalsum//totalcount])
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
        print(node)
        ans=0
        for i,j in node:
            if i==j:
                ans+=1
        return ans
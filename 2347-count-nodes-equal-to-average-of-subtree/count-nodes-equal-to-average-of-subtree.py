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
            global sum,count
            if root is None:
                return
            sum+=root.val
            count+=1
            preorder(root.left)
            preorder(root.right)
        stack=[root]
        while stack:
            current=stack.pop()
            preorder(current)
            node.append([current.val,sum//count])
            sum =0
            count=0
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
        print(node)
        ans=0
        for i in node:
            if i[0]==i[1]:
                ans+=1
        return ans
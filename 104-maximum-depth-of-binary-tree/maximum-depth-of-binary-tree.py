# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth=0

        if root:
            ls=[root]
            while ls:
                sublist=[]
                for temp in ls:
                    if temp.left:
                        sublist.append(temp.left)
                    if temp.right:
                        sublist.append(temp.right)
                ls=sublist
                depth+=1
        return depth

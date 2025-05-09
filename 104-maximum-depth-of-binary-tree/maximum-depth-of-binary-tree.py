# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        depth=0
        level=[root]
        while level:
            subnodes=[]
            for node in level:
                if node.left:
                    subnodes.append(node.left)
                if node.right:
                    subnodes.append(node.right)
            level=subnodes
            depth+=1
        return depth
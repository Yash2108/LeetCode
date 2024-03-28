# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # get depth of left node
        # get depth of right node
        # if difference >1, return False else return True
        def getDepth(node):

            if not node:
                return [ True, 0]
    
            l=getDepth(node.left)
            if not l[0]:
                return [False, l[1]+1]

            r=getDepth(node.right)
            if not r[0]:
                return [False, r[1]+1]

            height=max(l[1], r[1])
            if abs(r[1]-l[1])>1:
                return [False, height+1]
            return [True, height+1]

        if not getDepth(root)[0]:
            return False
        else:
            return True
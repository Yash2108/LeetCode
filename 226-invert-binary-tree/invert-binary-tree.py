# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        q = [root]

        while q:
            temp=q.pop(0)

            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
                
            temp.left, temp.right = temp.right, temp.left
        return root
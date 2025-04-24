# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        def dfs(node):
            if not node:
                return
            if node.val == p.val or node.val==q.val:
                return node
            left = dfs(node.left)
            right = dfs(node.right)

            if left: 
                if right:
                    return node
                else:
                    return left
            else:
                return right

        return dfs(root)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        '''
        dfs on p
        dfs on q
        compare
        '''

        def dfs(node, ls=[]):
            if not node:
                ls.append(None)
                return ls
            ls.append(node.val)
            dfs(node.left, ls)
            dfs(node.right, ls)
            return ls
        
        p_nodes=dfs(p, [])
        q_nodes=dfs(q, [])
        return p_nodes==q_nodes
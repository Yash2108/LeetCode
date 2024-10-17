# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def traverse(node, visited=[]):
            
            if node:
                visited.append(node.val)
                traverse(node.left, visited)
                traverse(node.right, visited)
            else:
                visited.append(None)
            return visited
        p_nodes=traverse(p, [])
        q_nodes=traverse(q, [])
        return p_nodes==q_nodes
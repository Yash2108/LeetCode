# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def dfs(root, visited=[]):
            if not root:
                visited.append(root)
                return visited
            visited.append(root.val)
            visited=dfs(root.left, visited)
            visited=dfs(root.right, visited)
            return visited
        
        toVisit=[root]
        subRoot_nodes=dfs(subRoot)
        while toVisit:
            node=toVisit.pop(0)
            if node:
                if dfs(node, [])==subRoot_nodes:
                    return True
                toVisit.append(node.left)                
                toVisit.append(node.right)                
        return False

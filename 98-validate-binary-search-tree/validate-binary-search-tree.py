# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, visited):
            if not root:
                return visited
            visited = dfs(root.left, visited)
            visited.append(root)
            visited = dfs(root.right, visited)
            return visited
        visited=dfs(root, [])
        visited=[i.val for i in visited]
        for i in range(len(visited)-1):
            if visited[i]>=visited[i+1]:
                return False
        return True
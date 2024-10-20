# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        visited=[root]
        result=[[root.val]]
        while visited:
            level=[]
            for node in visited:
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            visited=level
            if level:
                result.append([i.val for i in level])
        return result
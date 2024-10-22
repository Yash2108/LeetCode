# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        visited=[]
        toVisit=[[root]]
        while toVisit:
            node=toVisit.pop(0)
            if not node:
                continue
            if max([i.val for i in node])<=node[-1].val:
                visited.append(node)
            if node[-1].left:
                new_nodes=node+[node[-1].left]
                toVisit.append(new_nodes)
            if node[-1].right:
                new_nodes=node+[node[-1].right]
                toVisit.append(new_nodes)
        return len(visited)

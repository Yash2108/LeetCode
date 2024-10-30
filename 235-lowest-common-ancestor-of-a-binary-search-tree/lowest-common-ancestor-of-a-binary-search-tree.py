# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        

        '''
        
        lets do dfs
        we search for p and store its ancestors in a stack
        then from this list of ancestors, we search for q.
        return the ancestor when we have found q 

        '''

        ancestors=[]

        current_node=root
        while current_node:
            ancestors.append(current_node)
            if current_node.val==p.val:
                break
            elif current_node.val<p.val:
                current_node=current_node.right
            else:
                current_node=current_node.left
        ancestors=ancestors[::-1]

        while ancestors:
            node=ancestors[0]

            while node:
                if node.val==q.val:
                    return ancestors[0]
                elif node.val<q.val:
                    node=node.right
                else:
                    node=node.left 
            ancestors.pop(0)
        

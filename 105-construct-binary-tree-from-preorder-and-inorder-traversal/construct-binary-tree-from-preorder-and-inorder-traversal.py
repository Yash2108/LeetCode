# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        '''
        in order = left, main, right
        pre order = main, left, right
        '''
        if preorder:
            root = TreeNode(preorder[0])
            loc_root=inorder.index(root.val)
            left=self.buildTree(preorder[1:1+loc_root], inorder[:loc_root])
            right=self.buildTree(preorder[1+loc_root:], inorder[1+loc_root:])
            root.left = left
            root.right = right 
            return root
        else:
            return
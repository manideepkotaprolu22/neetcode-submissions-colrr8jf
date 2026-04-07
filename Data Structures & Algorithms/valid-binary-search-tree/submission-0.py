# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def binary(node,min,max):
            if not node:
                return True
            if node.val <= min or node.val >= max:
                return False
            
            return binary(node.left,min,node.val) and binary(node.right,node.val,max)

        return binary(root,float('-inf'),float('inf'))

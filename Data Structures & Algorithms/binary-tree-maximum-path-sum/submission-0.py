# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        self.max = float('-inf')

        def dfs(node):
            if not node:
                return 0

            left_max = dfs(node.left)
            right_max = dfs(node.right)
            
            left = max(0,left_max)
            right = max(0,right_max)

            current = node.val + left + right

            self.max = max(self.max,current)

            return node.val + max(left,right)
        
        dfs(root)
        return self.max
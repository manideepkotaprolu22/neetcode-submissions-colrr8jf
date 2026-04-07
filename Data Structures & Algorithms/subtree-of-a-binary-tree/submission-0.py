# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def same_tree(p,q):
            if not p and not q:
                return True
            if (p and not q) or (not p and q):
                return False
            if p.val != q.val:
                return False
            return same_tree(p.left,q.left) and same_tree(p.right,q.right)

        def sub_tree(root):
            if not root:
                return False
            if same_tree(root,subRoot):
                return True
            return sub_tree(root.left) or sub_tree(root.right)

        return sub_tree(root)



        
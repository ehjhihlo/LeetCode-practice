# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        return self.Sym(root.left, root.right)
    
    def Sym(self, left, right):
        if left == None and right == None:
            return True
        if not left or not right:
            return False
        if left.val != right.val:
            return False
        return self.Sym(left.left, right.right) and self.Sym(left.right, right.left)

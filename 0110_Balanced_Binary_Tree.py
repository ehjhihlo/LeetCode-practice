# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        depth = 0
        if not root:
            return True
        depth_left = self.getDepth(root.left)
        depth_right = self.getDepth(root.right)
        if abs(depth_left - depth_right) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False
        
    def getDepth(self, root):
        if root == None:
            return 0
        return 1 + max(self.getDepth(root.left), self.getDepth(root.right))

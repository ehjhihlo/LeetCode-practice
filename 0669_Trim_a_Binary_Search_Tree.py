# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val > high:
            return self.trimBST(root.left, low, high)
        if root.val < low:
            return self.trimBST(root.right, low, high)
        else:
            root.left = self.trimBST(root.left, low, high)
            root.right = self.trimBST(root.right, low, high)
            return root
# 說明：如果root的值比high大，表示root以及其所有右節點都不在這個區間內，向左搜尋。如果root的值比low小，表示root以及其所有左節點都不在這個區間內，向右搜尋。如果root正好在這個區間內，就對它左右子樹進行裁剪

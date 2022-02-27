# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        ans = 0
        if not root:
            return 0
        if not root.left:
            return 1 + self.minDepth(root.right)
        elif not root.right:
            return 1 + self.minDepth(root.left)
        else:
            return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
        return ans
#一個Node的最小高度不一定是兩個子樹的最小高度中較小的，當一個子樹為空時，該節點的最小高度等於另一個子樹的最小高度

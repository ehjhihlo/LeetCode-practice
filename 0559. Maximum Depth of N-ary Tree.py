"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
# DFS
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        if not root.children:
            return 1
        depth = 1 + max(self.maxDepth(child) for child in root.children)
        return depth

# BFS 
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        depth = 0
        queue = collections.deque()
        queue.append(root)
        
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                for child in node.children:
                    queue.append(child)
            depth += 1
        return depth

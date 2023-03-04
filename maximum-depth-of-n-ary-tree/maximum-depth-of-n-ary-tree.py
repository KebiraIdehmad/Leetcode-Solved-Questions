"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        answer = 0
        if not root:return 0
        
        def dfs(node, depth):
            nonlocal answer
            if not node : return 
            if not node.children:
                answer = max(answer, depth+1)
            for c in node.children:
                dfs(c, depth+1)
        dfs(root, 0)
        return answer
        

            
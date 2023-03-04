"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        depth = 0
        if not root:return 0
        
        def bfs(root):
            nonlocal depth
            q = deque([root])
            while q:
                for i in range(len(q)):
                    node = q.popleft()
                    if node.children:
                        for c in node.children:
                            q.append(c)
                depth+=1 
        bfs(root)
        return depth
        
        
        
                    

            
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        output = []
        def dfs(node):
            if not node.children:
                 return
            for c in node.children:
                dfs(c)
                output.append(c.val)
            
        if not root:return []
        dfs(root)
        output.append(root.val)
        return output
          
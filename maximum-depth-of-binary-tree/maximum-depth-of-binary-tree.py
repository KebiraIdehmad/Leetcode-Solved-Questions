# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:return 0
        answer = 0
        def dfs(node, depth):
            if not node :return 
            nonlocal answer
            if not node.left and not node.right:
                answer = max(answer, depth+1)
                
            dfs(node.left, depth+1)
            dfs(node.right, depth+1)
        dfs(root, 0)
        return answer
            
        
        












                

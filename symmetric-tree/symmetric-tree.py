# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def helper(leftroot, rightroot):
            if not leftroot and not rightroot:return True
            
            if (not leftroot and rightroot) or ( leftroot and not rightroot) or leftroot.val !=  rightroot.val: return False
            return helper(leftroot.left, rightroot.right) and helper(leftroot.right, rightroot.left)
        if not root.left and not root.right: return True
        return helper(root.left, root.right)
            
        
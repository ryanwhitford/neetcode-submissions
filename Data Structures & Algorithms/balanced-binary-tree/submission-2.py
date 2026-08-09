# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True
        def maxDepth(root):
            if not root:
                return 0
            dl = maxDepth(root.left)
            dr = maxDepth(root.right)
            nonlocal res
            if abs(dl - dr) > 1:
                res = False
            return 1 + max(dl,dr)
        maxDepth(root)
        return res
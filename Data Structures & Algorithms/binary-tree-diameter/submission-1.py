# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        d = 0
        def maxDepth(root):
            if not root:
                return 0
            nonlocal d
            d = max(d, maxDepth(root.left) + maxDepth(root.right))
            return 1 + max(maxDepth(root.left),maxDepth(root.right))
        maxDepth(root)
        return d
        
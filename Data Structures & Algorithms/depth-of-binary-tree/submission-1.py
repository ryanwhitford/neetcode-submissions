# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        d = 0
        maxd = d
        def backtrack(root):
            nonlocal d, maxd
            if not root:
                return
            d+=1
            maxd = max(d,maxd)
            backtrack(root.left)
            backtrack(root.right)
            d-=1
        backtrack(root)
        return maxd


            
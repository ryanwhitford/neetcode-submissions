# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def backtrack(curr, maxval):
            nonlocal res
            if not curr:
                return
            if maxval <= curr.val:
                res+=1
            newmaxval = max(maxval, curr.val)
            if curr.left:
                backtrack(curr.left, newmaxval)
            if curr.right:
                backtrack(curr.right, newmaxval)
            return
        backtrack(root, float("-infinity"))
        return res
            
            
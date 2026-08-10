# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # enforce p < q
        if p.val > q.val:
            p, q = q, p
        res = TreeNode()
        def backtrack(root):
            nonlocal p, q, res
            if not root:
                return
            if p.val <= root.val <= q.val:
                res = root
            elif root.left and p.val <= root.val and q.val <= root.val:
                backtrack(root.left)
            elif root.right and root.val <= q.val and root.val <= p.val:
                backtrack(root.right)
            return
        backtrack(root)
        return res
            

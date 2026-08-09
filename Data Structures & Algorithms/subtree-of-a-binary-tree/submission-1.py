# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(t1,t2):
            if not t1 and not t2:
                return True
            elif not t1 or not t2:
                return False
            elif t1.val != t2.val:
                return False
            else:
                return isSameTree(t1.left,t2.left) and isSameTree(t1.right,t2.right)
        def backtrack(root, subRoot):
            if not root:
                return False
            elif isSameTree(root,subRoot):
                return True
            else:
                b1 = backtrack(root.left, subRoot)
                b2 = backtrack(root.right, subRoot)
                return b1 or b2
        return backtrack(root,subRoot)
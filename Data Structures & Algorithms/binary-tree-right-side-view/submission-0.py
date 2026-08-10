# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = [root.val]
        queue = deque([root])

        while queue:
            layer_size = len(queue)
            layer = []
            for _ in range(layer_size):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                    layer.append(curr.left.val)
                if curr.right:
                    queue.append(curr.right)
                    layer.append(curr.right.val)
            if layer:
                res.append(layer[-1])
        return res
        
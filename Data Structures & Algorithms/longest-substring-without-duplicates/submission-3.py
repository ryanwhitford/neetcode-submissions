class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        stack = []
        seen = set()
        for c in s:
            while stack and c in stack:
                stack.pop(0)
            stack.append(c)
            res = max(res, len(stack))
        return res

            
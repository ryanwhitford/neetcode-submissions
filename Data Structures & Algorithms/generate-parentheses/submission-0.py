class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack, res = [], []
        def backtrack(o, c):
            if c == n:
                s = "".join(stack)
                res.append(s)
                return
            if o < n:
                stack.append("(")
                backtrack(o+1, c)
                stack.pop()
            if c < o:
                stack.append(")")
                backtrack(o, c+1)
                stack.pop()
            return
        backtrack(0,0)
        return res
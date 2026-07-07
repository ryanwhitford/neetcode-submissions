class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for s in tokens:
            if s not in "+-*/":
                stack.append(int(s))
                continue
            elif s == "+":
                x = stack[-1] + stack[-2]
            elif s == "-":
                x = stack[-2] - stack[-1]
            elif s == "*":
                x = stack[-1] * stack[-2]
            elif s == "/":
                x = int(stack[-2] / stack[-1])
            stack.pop()
            stack.pop()
            stack.append(x)
        return stack[0]
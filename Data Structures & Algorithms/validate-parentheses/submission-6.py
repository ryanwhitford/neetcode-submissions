class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close2open = {')':'(', ']':'[','}':'{'}
        for c in s:
            if c in "([{":
                stack.append(c)
            elif c in ")]}":
                if stack and close2open[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                print("invalid string")
                return
        return True if not stack else False
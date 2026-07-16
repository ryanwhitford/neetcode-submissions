class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        stack = []
        res = []
        candidates.sort()
        def backtrack(target, i):
            if target == 0:
                res.append(list(stack))
                return
            for j in range(i+1, len(candidates)):
                if j > i + 1 and candidates[j] == candidates[j-1]:
                    continue
                num = candidates[j]
                if target - num < 0:
                    break
                stack.append(num)
                backtrack(target - num, j)
                stack.pop()
        backtrack(target,-1)
        return res
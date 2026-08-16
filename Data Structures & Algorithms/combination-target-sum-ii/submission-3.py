class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        stack = []
        res = []
        candidates.sort()
        def backtrack(i, curr):
            if curr == target:
                res.append(list(stack))
                return
            if i == len(candidates) or curr > target:
                return
            # with
            stack.append(candidates[i])
            backtrack(i+1, curr + candidates[i])
            stack.pop()

            #without
            while i < len(candidates)-1 and candidates[i] == candidates[i+1]:
                i+=1
            backtrack(i+1, curr)
            
            return
        backtrack(0, 0)
        return res
            
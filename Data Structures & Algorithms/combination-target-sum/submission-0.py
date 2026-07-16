class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        stack = []
        def backtrack(target, j):
            if target == 0:
                res.append(list(stack))
                return
            for i in range(j, len(nums)):
                num = nums[i]
                if num <= target:
                    stack.append(num)
                    backtrack(target-num, i)
                    stack.pop()
        backtrack(target, 0)
        return res

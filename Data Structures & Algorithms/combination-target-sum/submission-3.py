class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        stack = []
        res = []
        def backtrack(i, curr):
            if curr == target:
                res.append(list(stack))
                return
            if i == len(nums) or curr > target:
                return
            stack.append(nums[i])
            backtrack(i, curr + nums[i])
            stack.pop()
            backtrack(i+1, curr)
            return
        backtrack(0, 0)
        return res
            

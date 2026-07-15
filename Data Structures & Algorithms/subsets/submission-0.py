class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        stack = []
        def backtrack(i):
            if i>=len(nums):
                res.append(list(stack))
                return
            p = nums[i]
            #without
            backtrack(i+1)
            #with
            stack.append(p)
            backtrack(i+1)
            stack.pop()

        backtrack(0)
        return res
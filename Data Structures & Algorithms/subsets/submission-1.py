class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        stack = []
        def backtrack(i):
            if i >= len(nums):
                res.append(list(stack))
                return
            # with
            stack.append(nums[i])
            backtrack(i+1)
            stack.pop()
            #without
            backtrack(i+1)
            return
        backtrack(0)
        return res

                
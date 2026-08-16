class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        stack = []
        def backtrack(i):
            if i == len(nums):
                res.append(stack.copy())
                return
            # with
            stack.append(nums[i])
            backtrack(i+1)
            stack.pop()
            # without
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i+=1
            backtrack(i + 1)
            return
        backtrack(0)
        return res
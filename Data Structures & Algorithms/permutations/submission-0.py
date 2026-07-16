class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        stack = []
        res = []
        def backtrack(nums):
            if len(nums) == 0:
                res.append(list(stack))
                return
            for i,num in enumerate(nums):
                stack.append(num)
                nums.pop(i)
                backtrack(nums)
                nums.insert(i, num)
                stack.pop()
        backtrack(nums)
        return res
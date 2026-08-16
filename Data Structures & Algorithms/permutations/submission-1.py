class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        stack = []
        res = []
        def backtrack(nums):
            if not nums:
                res.append(stack.copy())
            for i, num in enumerate(nums): 
                stack.append(num)
                nums.pop(i)
                backtrack(nums)
                stack.pop()
                nums.insert(i, num)
            return
        backtrack(nums)
        return res
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        stack = []
        def backtrack(remainder, i):
            if i >= len(nums) or remainder < 0:
                return
            if remainder == 0:
                res.append(list(stack))
                return
            num = nums[i]
            stack.append(num)
            backtrack(remainder-num, i)
            stack.pop()
            backtrack(remainder, i+1)
            return        
        backtrack(target, 0)    
        return res

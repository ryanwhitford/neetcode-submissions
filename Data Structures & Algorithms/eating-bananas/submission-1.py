class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxPile = max(piles)
        l, r = 1, maxPile
        res = float("infinity")
        while l<=r:
            i = (l+r)//2
            hours = 0
            for pile in piles:
                hours += -((-pile) // i)
            if hours <= h:
                res = min(res, i)
                r=i-1
            elif hours > h:
                l=i+1
        return res

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        minPrice = float("infinity")
        for price in prices:
            minPrice = min(minPrice, price)
            res = max(price-minPrice, res)
        return res
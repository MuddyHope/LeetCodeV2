class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        l, r = 0, 1
        profit_so_far = 0
        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
            elif prices[l] < prices[r]:
                profit_so_far = prices[r] - prices[l]
                max_profit = max(profit_so_far, max_profit)
            r += 1
        return max_profit

        
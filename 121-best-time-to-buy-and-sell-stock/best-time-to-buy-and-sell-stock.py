class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # sliding window

        i, j = 0, 1
        max_profit = 0
        while j < len(prices):
            if prices[j] < prices[i]:
                i = j  # move buy pointer to the cheaper price
            profit_so_far = prices[j] - prices[i]
            max_profit = max(max_profit, profit_so_far)
            j += 1

        return max_profit
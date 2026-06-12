class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j = 0, 1
        max_profit = 0
        while j < len(prices):
            # print(f"checking for prices: {prices[i], i, prices[j], j}")
            if prices[i] >= prices[j]:       # no chance of making a profit
                i = j

            elif prices[i] < prices[j]:
                max_profit = max(max_profit, prices[j] - prices[i])
            j += 1

        return max_profit

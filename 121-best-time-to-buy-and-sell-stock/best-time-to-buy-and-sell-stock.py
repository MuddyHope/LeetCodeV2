class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        first = prices[0]
        profitSofar = 0
        for i in range(1, len(prices)):
            first = min(prices[i], first)
            profitSofar = max(profitSofar, prices[i] - first)

        return profitSofar
            
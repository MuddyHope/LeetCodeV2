class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        first = prices[0]
        profitSofar = 0
        for i in range(len(prices)):
            if prices[i] < first:
                first = prices[i]
            elif prices[i] - first >= profitSofar:
                profitSofar = prices[i] - first
            # print(profitSofar)

        return profitSofar
            
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        i, j = 0, 0

        res = 0

        while j < len(prices):
            print(f"i: {i}, j: {j}")
            if prices[j] < prices[i]:
                i = j
            
            if prices[j] - prices[i] > res:
                res = prices[j] - prices[i]
            
            j += 1
        return res
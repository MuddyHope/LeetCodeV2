class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        profit_so_far = 0
        first = prices[0]
        for each_price in prices:
            if each_price < first:
                first = each_price
            elif profit_so_far < each_price - first:
                profit_so_far = each_price - first
                max_profit += profit_so_far
                first = each_price
                profit_so_far = 0
            print(f"each_price: {each_price}, first: {first}, max_profit: {max_profit}")
        return max_profit
        
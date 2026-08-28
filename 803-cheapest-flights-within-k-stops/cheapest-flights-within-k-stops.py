class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        

        # bellman-ford

        prices = [float("inf")] * n
        prices[src] = 0

        for _ in range(k+1):
            temp = prices.copy()

            for s, d, price in flights:
                if prices[s] == float("inf"):
                    continue
                
                if price + prices[s] < temp[d]:
                    temp[d] = price + prices[s]
            prices = temp 
        return -1 if  prices[dst] == float("inf") else prices[dst]
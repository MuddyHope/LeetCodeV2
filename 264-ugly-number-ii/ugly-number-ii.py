import heapq

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = [1]
        seen = set([1])
        factors = [2, 3, 5]
        
        for _ in range(n):
            ugly = heapq.heappop(heap)
            for f in factors:
                new_ugly = ugly * f
                if new_ugly not in seen:
                    seen.add(new_ugly)
                    heapq.heappush(heap, new_ugly)
                    
        return ugly

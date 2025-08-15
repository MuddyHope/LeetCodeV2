class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []
        heapify(maxHeap)
        for each_stone in stones:
            heappush(maxHeap, -(each_stone))
        
        while maxHeap:
            if len(maxHeap) == 1:
                return -maxHeap[0]
            biggest = heappop(maxHeap)
            second_biggest = heappop(maxHeap)
            _ = biggest - second_biggest
            heappush(maxHeap, _)
        

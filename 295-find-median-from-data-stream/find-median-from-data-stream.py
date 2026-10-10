class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        
        if not self.maxHeap or num <= -self.maxHeap[0]:
            heapq.heappush(self.maxHeap, -num)
        
        else:
            heapq.heappush(self.minHeap, num)

        if len(self.maxHeap) > len(self.minHeap) +1:
            largest = -heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, largest)
        
        elif len(self.minHeap) > len(self.maxHeap):
            smallest = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -smallest)

    def findMedian(self) -> float:

        if len(self.minHeap) < len(self.maxHeap):
            return -self.maxHeap[0]
        
        
        return (self.minHeap[0] + -self.maxHeap[0]) /2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
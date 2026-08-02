class MinStack:

    def __init__(self):
        self.stack = []
        self.minHeap = []
        
    def push(self, value: int) -> None:
        self.stack.append(value)
        heapq.heappush(self.minHeap, value)

    def pop(self) -> None:
        val = self.stack.pop()
        self.minHeap[:] = self.stack
        heapq.heapify(self.minHeap)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minHeap[0]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
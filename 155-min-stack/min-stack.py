class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = [float(inf)]

    def push(self, value: int) -> None:
        # print(f"stack: {self.stack}, min_stack: {self.min_stack}")
        self.stack.append(value)
        if self.min_stack[-1] >= value:
            self.min_stack.append(value)

    def pop(self) -> None:
        # print(f"stack: {self.stack}, min_stack: {self.min_stack}")
        val = self.stack.pop()
        if self.min_stack[-1] == val:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.min_stack[-1]




# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
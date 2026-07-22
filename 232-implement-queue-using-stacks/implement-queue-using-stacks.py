class MyQueue:

    def __init__(self):
        self.stack = [] 
        self.help_stack = []      

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        return self.helper_fun(peek=False)
        

    def peek(self) -> int:
        return self.helper_fun(peek=True)
        

    def empty(self) -> bool:
        if len(self.stack) >= 1:
            return False
        return True
    
    def helper_fun(self, peek=False) -> res:
        while self.stack:
            self.help_stack.append(self.stack.pop())
        res = self.help_stack.pop() if not peek else self.help_stack[-1]
        while self.help_stack:
            self.stack.append(self.help_stack.pop())
        return res
        

        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
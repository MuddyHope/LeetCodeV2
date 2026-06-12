class MyQueue:

    def __init__(self):
        self.stack = []
        self.hash = {}
        self.counter = 0

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.hash[self.counter] = x
        self.counter += 1

    def pop(self) -> int:
        res = self.stack[0]
        del self.stack[0]
        self.reduce_hashmap()
        return res

    def peek(self) -> int:
        return self.stack[0]

    def empty(self) -> bool:
        return False if len(self.stack) else True

    def reduce_hashmap(self):
        print(f"hash: {self.hash}")
        temp = self.hash.copy()
        for idx, num in temp.items():
            if idx == 0:
                del self.hash[idx]
                continue
            self.hash[idx-1] = num
        print(f"after: {self.hash}")
        

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
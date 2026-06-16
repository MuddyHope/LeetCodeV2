class FreqStack:

    def __init__(self):
        self.hash = {}  # val, count
        self.group = defaultdict(list) # freq, [vals]
        self.max_freq = 0

    def push(self, val: int) -> None:
        self.hash[val] = 1 + self.hash.get(val, 0)

        _g = self.hash[val]
        if _g > self.max_freq:
            self.max_freq = _g
        
        self.group[_g].append(val)

        

    def pop(self) -> int:
        val = self.group[self.max_freq].pop()

        self.hash[val] -=1

        if not self.group[self.max_freq]:
            self.max_freq -= 1

        return val

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
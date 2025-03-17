class MyHashMap:
    def __init__(self):
        self.n = 10000
        self.arr = [[] for _ in range(self.n)]

    def put(self, key: int, value: int) -> None:
        idx = key % self.n
        for i, (k, v) in enumerate(self.arr[idx]):
            if k == key:
                self.arr[idx][i] = (key, value)
                return
        self.arr[idx].append((key, value))

    def get(self, key: int) -> int:
        idx = key % self.n
        for k, v in self.arr[idx]:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        idx = key % self.n
        self.arr[idx] = [(k, v) for k, v in self.arr[idx] if k != key]
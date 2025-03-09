class TimeMap:

    def __init__(self):
        self.hash_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.hash_map.keys():
            self.hash_map[key] = []
        self.hash_map[key].append((value, timestamp))


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hash_map:
            return ""
        
        values = self.hash_map[key]
        left, right = 0, len(values) - 1
        res = ""
        
        while left <= right:
            mid = (left + right) // 2
            if values[mid][1] <= timestamp:
                res = values[mid][0]
                left = mid + 1
            else:
                right = mid - 1
        return res
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
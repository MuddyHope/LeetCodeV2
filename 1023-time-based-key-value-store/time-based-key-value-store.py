class TimeMap:

    def __init__(self):
        self.hash_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hash_map[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        # binary search or the left, as they are ascending
        if key not in self.hash_map:
            return ""
        vals: List[int] = self.hash_map.get(key)
        # print(f"vals: {vals}, key: {key}, timestamp: {timestamp}")
        l, r = 0, len(vals) -1
        res = ""
        while l <= r:
            mid = (l+r)//2
            # print(f"l: {l}, mid: {mid}, r: {r}")
            curr_key, curr_timestamp = vals[mid]
            if curr_timestamp <= timestamp:
                l = mid + 1
                res = vals[mid][0]
            else:
                r = mid - 1
        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
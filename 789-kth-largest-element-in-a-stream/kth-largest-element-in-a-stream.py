class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        # self.max_heap = [-x for x in nums]
        # heapq.heapify(self.max_heap)
        self.k = k
        self.nums = sorted(nums, reverse=True)

    def add(self, val: int) -> int:
        # heapq.heappush(self.max_heap, -val)
        # print(list(self.max_heap))
        # res = self.max_heap[self.k-1]
        self.nums.append(val)
        self.nums = sorted(self.nums, reverse=True)
        return self.nums[self.k-1]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
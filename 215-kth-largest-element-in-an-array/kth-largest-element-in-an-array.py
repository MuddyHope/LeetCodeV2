class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        
        counter = Counter(nums)
        hq = []
        for val, freq in counter.items():
            heapq.heappush(hq, (-val, freq))
        
        print(list(hq))
        i = 0
        while i < k:
            key, freq = heapq.heappop(hq)
            i += freq

            if i >= k:
                return -key
        # return hq[0]
            
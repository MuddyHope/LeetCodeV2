from collections import Counter
import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:

        counter = Counter(nums)
        hq = []

        for num, freq in counter.items():
            heapq.heappush(hq, (-num, freq))

        i = 0

        while hq:
            num, freq = heapq.heappop(hq)

            i += freq

            if i >= k:
                return -num
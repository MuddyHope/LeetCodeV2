from typing import List
import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        heap = []
        res = []

        for i in range(len(nums)):

            # push negative value to simulate max heap
            heapq.heappush(heap, (-nums[i], i))

            # remove elements outside window
            while heap[0][1] <= i - k:
                heapq.heappop(heap)

            # start recording results once window reaches size k
            if i >= k - 1:
                res.append(-heap[0][0])

        return res
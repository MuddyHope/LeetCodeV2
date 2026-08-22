class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        #heap??
        heap = []
        for each in nums:
            heapq.heappush(heap, (-each))

        i = 0
        while i < k:
            vals = heapq.heappop(heap)
            # print(f"i: {i}, vals: {vals}")
            i += 1
        return -vals
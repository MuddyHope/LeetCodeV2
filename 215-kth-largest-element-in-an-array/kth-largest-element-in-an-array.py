import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heapq.heapify(nums)
        while len(nums) > k:
            v = heapq.heappop(nums)
        return nums[0]
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heapq.heapify(nums)
        print("len", nums)
        while len(nums) > k:
            v = heapq.heappop(nums)
            print("curr", v)
        return nums[0]
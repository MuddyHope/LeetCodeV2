class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_res = nums[0]

        total = 0
        for i in range(len(nums)):
            if total < 0:
                total = 0
            
            total += nums[i]
            max_res = max(total, max_res)
        return max_res
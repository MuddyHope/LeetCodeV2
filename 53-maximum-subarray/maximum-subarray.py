class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        
        l, r = 0, 1
        res_so_far = nums[l]

        max_res = nums[l]

        while r < len(nums):
            if nums[r] + res_so_far < nums[r]:
                res_so_far = nums[r]
                l = r
            else:
                res_so_far += nums[r]
            r += 1
            max_res = max(res_so_far, max_res)
        
        return max_res
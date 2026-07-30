class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        
        l, r = 0, 1
        max_res = nums[0]
        
        res_so_far = nums[0]
        while r < len(nums):
            if nums[r] + res_so_far < nums[r]:
                res_so_far = nums[r]
                l = r
            else:
                res_so_far += nums[r]
            max_res = max(res_so_far, max_res)
            r += 1
        return max_res
        
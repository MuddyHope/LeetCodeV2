class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = 0
        
        if len(nums) == 1:
            if target <= nums[0]:
                return 1
            else :
                return res
    
        left = 0
        res = float("inf")

        right = 1
        curr_sum = 0

        for right in range(len(nums)):
            curr_sum += nums[right]
            while curr_sum >= target:
                res = min(res, right - left + 1)
                curr_sum -= nums[left]
                left += 1
            right += 1
            
        return res if res != float("inf") else 0
        
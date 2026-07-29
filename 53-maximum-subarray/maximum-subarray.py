class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]

        max_res = nums[0]
        i , j = 0, 1

            
        #   0 -2 -1 -5 -1 -2 0 1 -4 0
        #  -3 -1 -2 5  1  2 0 -1 4 0
        res_so_far = nums[0]
        while j < len(nums):
            print(f"i: {i}, j: {j}")
            if res_so_far + nums[j] < nums[j]:
                res_so_far = nums[j]
                i = j
            else:
                res_so_far += nums[j]
            max_res = max(res_so_far, max_res)
        
            j += 1
        return max_res


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        left, right = 0, 1
        max_diff = -1
        max_diff_so_far = 0
        while right < len(nums):
            if nums[left] < nums[right]:
                max_diff_so_far = nums[right] - nums[left]
                max_diff = max(max_diff_so_far, max_diff)
            else:
                left = right
            right += 1
            print(max_diff)
        return max_diff
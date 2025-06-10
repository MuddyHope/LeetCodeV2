class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        left, right = 0, 1
        max_diff = -1
        max_diff_so_far = -1
        while right < len(nums):
            if nums[right] > nums[left]:
                max_diff_so_far = nums[right] - nums[left]
                print(left, right, max_diff_so_far)
                max_diff = max(max_diff_so_far, max_diff)
            else:
                left = right
            right += 1

        return max_diff
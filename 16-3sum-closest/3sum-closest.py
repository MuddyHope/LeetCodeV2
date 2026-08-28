class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nums.sort()

        res = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):

            left = i + 1
            right = len(nums) - 1

            while left < right:

                curr_sum = nums[i] + nums[left] + nums[right]

                # Update closest answer
                if abs(curr_sum - target) < abs(res - target):
                    res = curr_sum

                # Exact match
                if curr_sum == target:
                    return curr_sum

                # Need a larger sum
                elif curr_sum < target:
                    left += 1

                # Need a smaller sum
                else:
                    right -= 1

        return res
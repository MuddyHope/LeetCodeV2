class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left, right = 0, k - 1
        max_average = -float("inf")
        current_sum = sum(nums[left:right+1])
        while right < len(nums):
            max_average = max(max_average, current_sum/k)
            right += 1
            if right < len(nums):  # avoid index error
                current_sum += nums[right]
                current_sum -= nums[left]
                left += 1

            # print(max_average)
        return max_average
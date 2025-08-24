class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        prev = 0
        count = 0
        max_len = 0
        found_zero = False

        for num in nums:
            if num == 1:
                count += 1
            else:
                max_len = max(max_len, prev + count)
                prev = count
                count = 0
                found_zero = True

        max_len = max(max_len, prev + count)

        if not found_zero:
            return len(nums) - 1

        return max_len
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        max_length = 0
        for each_number in numset:
            if each_number - 1 not in numset:
                length = 1
                while each_number + length in numset:
                    length += 1
                max_length = max(length, max_length)
        return max_length

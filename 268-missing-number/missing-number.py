class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numSet = set(nums)

        i = 0
        while i <= len(numSet):
            _len = 0
            if _len + i not in numSet:
                return _len + i
            _len += 1
            i += 1
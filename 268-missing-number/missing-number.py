class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        

        numSet = set(nums)
        _len = 0
        for i in range(len(numSet)):
            while _len + i in numSet:
                _len += 1
            return _len
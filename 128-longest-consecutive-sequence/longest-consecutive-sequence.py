class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numSet = set(nums)
        res = 0

        for each in numSet:
            if (each - 1) not in numSet:            # check which is the beginning of the sequence
                i = 0 
                while (each+i) in numSet:
                    i += 1
                res = max(res, i)
        return res
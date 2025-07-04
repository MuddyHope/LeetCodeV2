class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        # find minimum of the numlist

        count_p = count_n = 0
        for i in nums:
            if i == 0:
                continue
            if i > 0:
                count_p += 1
            else:
                count_n += 1
        return max(count_p, count_n)

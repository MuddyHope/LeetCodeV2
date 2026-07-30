class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        set_nums = set(nums)
        n = len(nums)
        k = len(set_nums)
        nums[:] = list(sorted(set_nums)) + (n-k) * [0]
        return k
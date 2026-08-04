class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        set_nums = set(nums)
        res = []
        _min, _max = min(nums), max(nums)

        for i in range(_min, _max):
            if i not in set_nums:
                res.append(i)
        return res
        

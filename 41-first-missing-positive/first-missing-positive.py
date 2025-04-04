class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        nums = set(nums)
        print(nums)
        print(max(nums))
        for i in range(1, max(nums)+2):
            print(f"i is {i}")
            if i not in nums:
                return i
        return 1
        
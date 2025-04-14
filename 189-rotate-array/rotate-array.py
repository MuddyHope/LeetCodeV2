class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0, len(nums)-1
        while left < k:
            last = nums.pop()
            nums.insert(0, last)
            right -= 1
            left += 1
        
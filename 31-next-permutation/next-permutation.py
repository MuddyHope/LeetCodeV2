class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # find the index, where it is smaller than the last idx

        pivot = len(nums) - 1
        while pivot > 0 and nums[pivot - 1] >= nums[pivot]:
            pivot -= 1
        print(nums[pivot])

        if pivot == 0:
            nums.reverse()
            return
        
        successor = len(nums) - 1
        while successor >= pivot and nums[successor] <= nums[pivot-1]:
            successor -= 1
        
        # swap
        nums[pivot-1], nums[successor] = nums[successor], nums[pivot-1]

        nums[pivot:] = reversed(nums[pivot:])

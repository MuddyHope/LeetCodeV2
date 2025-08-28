class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # [2,3,4,1,6,5] -> [2,3,4,5,1,6]
        
        n = len(nums) - 1
        i = n
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        print(i)

        if i == 0:
            nums.reverse()
            return
        # now find j
        j = n

        while j >= i and nums[j] <= nums[i-1]:
            j -= 1
        
        nums[i-1], nums[j] = nums[j], nums[i-1]
        nums[i:] = reversed(nums[i:])
        
       




        
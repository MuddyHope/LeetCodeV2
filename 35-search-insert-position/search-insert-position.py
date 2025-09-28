class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # binary search
        total_len = len(nums)
        # finding mid point for the loop.
        mid_point = total_len//2
        '''
        1) find mid point until ?
        2) case1: if found return index
        3) case2: if not found, if next index is greater than target, return that index
        '''
        if nums[mid_point] == target:
            return mid_point
        # check left and right if the numbers are less than the current number
        # nums = [1, 2, 4, 8, 12, 14, 18]
        left, right = 0, len(nums) -1
        while left <= right:
            print("left is ", left)
            mid = (left+right)//2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
        return left


            
    
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        if len(nums) == 1 and nums[0] == target:
            return 0
    
        l, r = 0, len(nums) -1

        while l <= r:
            mid = (l+r) //2
            if target > nums[mid]:
                l = mid +1
            elif target < nums[mid]:
                r = mid - 1
            else:
                return mid
        return -1
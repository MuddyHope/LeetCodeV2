class Solution:
    def findMin(self, nums: List[int]) -> int:
        # find max, then go next step
        l, r = 0, len(nums)-1
        min_so_far = float("+inf")
        while l<=r:
            mid = (l+r)//2
            min_so_far = min(min_so_far, nums[mid])
            if nums[r] < nums[mid]:
                l = mid+1
            else:
                r = mid - 1
        return min_so_far
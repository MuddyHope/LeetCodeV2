class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = (nums1 + nums2)
        nums.sort()
        mid = len(nums)//2

        if len(nums) % 2 == 0:
            print(nums)
            return float((nums[mid] + nums[mid-1]) /2)
        return float(nums[mid])
        
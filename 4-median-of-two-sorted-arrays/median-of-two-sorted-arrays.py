class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num = sorted(nums1 + nums2)
        n = len(num)
        print(num)
        if n % 2 == 0:
            return (num[n//2] + num[(n//2)-1])/2
        return num[n//2]

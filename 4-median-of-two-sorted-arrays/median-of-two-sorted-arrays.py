class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n, m = len(nums1), len(nums2)

        nums3 = []
        i = j = 0
        while i < n and j < m:
            if nums1[i] > nums2[j]:
                nums3.append(nums2[j])
                j += 1
            else:
                nums3.append(nums1[i])
                i += 1

        while i < n:
            nums3.append(nums1[i])
            i += 1

        while j < m:
            nums3.append(nums2[j])
            j += 1

        # now that we have sorted array, lets find the median
        mid = len(nums3)//2
        print(nums3)
        if len(nums3) % 2 != 0:
            return float(nums3[mid])   
        return float((nums3[mid] + nums3[mid-1])/2)

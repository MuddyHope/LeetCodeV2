class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # binary search to find the tipping point

        l , r = 0, len(nums) -1

        while l < r:
            mid = (l+r) //2
            print(f"l: {l}, mid: {mid}, r: {r}")
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        return nums[l]
            
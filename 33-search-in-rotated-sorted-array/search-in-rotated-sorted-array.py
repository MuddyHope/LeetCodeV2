class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums) -1

        while l <= r:
            mid = (l+r)//2
            print(f"l:{l}, mid: {mid}, r: {r}")
            if nums[mid] == target:
                return mid
            
            if nums[l] == target:
                return l
            if nums[r] == target:
                return r
            if nums[l] <= nums[mid]:
                if nums[l] <= target <= nums[mid]:
                    r = mid
                else:
                    l = mid + 1
            
            elif nums[r] <= nums[mid]:
                if nums[mid] <= target <= nums[r]:
                    l = mid
                else:
                    r = mid - 1
            else:
                l += 1
                r -= 1
        return -1
            
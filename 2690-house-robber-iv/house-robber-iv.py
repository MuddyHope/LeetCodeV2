class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        
        l = min(nums)
        r = max(nums)
        res = r

        while l <= r:
            mid = (l+r)//2
            ret = self.helper(nums, mid, k)
            if ret:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res

    def helper(self, nums, mid, k):
        cnt = 0

        i = 0
        while i < len(nums):
            if nums[i] <= mid:
                # we have already robbed this house
                cnt += 1
                i += 2
            else:
                i += 1
            # print(f"mid: {mid}, temp: {temp}")
            if cnt >= k:
                return True
    
        return False
            

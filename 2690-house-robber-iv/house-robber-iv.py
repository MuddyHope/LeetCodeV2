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
        temp = []

        i = 0
        while i < len(nums):
            if nums[i] <= mid:
                # we have already robbed this house
                temp.append(nums[i])
                i += 2
            else:
                i += 1
            # print(f"mid: {mid}, temp: {temp}")
            if len(temp) >= k:
                return True
    
        return False
            

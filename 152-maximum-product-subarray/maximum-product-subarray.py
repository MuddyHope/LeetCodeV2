class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        

        res = max(nums)

        curMin, curMax = 1, 1

        for n in nums:
            
            temp = curMax *n
            curMax = max(curMin*n, curMax*n, n)
            curMin = min(curMin*n, temp, n)
            res = max(curMax, res)
        return res
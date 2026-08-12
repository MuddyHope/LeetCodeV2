class Solution:
    def rob(self, nums: List[int]) -> int:
        
        dp = [0] * (len(nums))
        dp[0] = nums[0]

        for i in range(len(nums)):
            print(f"i: {i}, dp: {dp}")
            if i >= 2:
                dp[i] = max(dp[i-1], nums[i] + dp[i-2])
                print(dp)
            else:
                dp[i] = max(nums[i], dp[i-1])
        return dp[-1]
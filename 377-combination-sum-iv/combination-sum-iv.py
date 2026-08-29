class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1

        for curr_sum in range(1, target + 1):
            for num in nums:
                if curr_sum - num >= 0:
                    dp[curr_sum] += dp[curr_sum - num]

        return dp[target]
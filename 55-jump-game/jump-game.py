class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)
        dp[0] = True

        for i in range(len(nums)):
            if dp[i]:
                for j in range(i + 1, min(len(nums), i + nums[i] + 1)):
                    dp[j] = True

        return dp[-1]
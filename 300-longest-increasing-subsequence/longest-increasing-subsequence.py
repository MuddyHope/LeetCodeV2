class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        dp = [1] * len(nums)

        # [10,9,2,5,3,7,101,18]
        # [1,0, 1, 1, 2, 3, 4, 0]


        # [0,1,0,3,2,3]
        # [1,2]
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
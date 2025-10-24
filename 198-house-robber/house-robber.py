class Solution:
    def rob(self, nums: List[int]) -> int:
        nums.extend([0,0])

        for i in range(len(nums) - 3, -1, -1):
            print(i)
            nums[i] = max(nums[i] + nums[i+2], nums[i+1])
            print(nums)
        return nums[0]     
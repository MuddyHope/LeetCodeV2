class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        # [-4,-1,-1,0,1,2]
        i = 0
        while i < len(nums) - 2:
            j = i + 1
            k = len(nums) - 1
            if i > 0 and nums[i] == nums[i-1]:
                i += 1
                continue
            while j < k:
                # print(i, j, k)
                curr_sum = nums[i] + nums[j] + nums[k]
                if curr_sum == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[k] == nums[k+1]:
                        k -=1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                elif curr_sum > 0:
                    k -= 1
                else:
                    j += 1
            i += 1
        return res

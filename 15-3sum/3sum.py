class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()

        i = 0

        res = []

        while i < len(nums) -2:
            l = i + 1
            r = len(nums) - 1
            while l < r:
               
                # print(f"i: {i}, l: {l}, r: {r}")

                curr_sum = nums[i] + nums[l] + nums[r]
                # print(f"curr_sum: {curr_sum}")
                if curr_sum == 0:
                    res.append([nums[i],nums[l],nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                elif curr_sum > 0:
                    r -= 1
                else:
                    l += 1
            i += 1

            while i < len(nums) -2 and nums[i] == nums[i-1]:
                i += 1
    
        return res

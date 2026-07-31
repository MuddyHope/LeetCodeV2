class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        l, r = 0, n -1
        res = []
        # [-1,0,1,2,-1,-4]
        # -4 -1 -1 0 1 2
        i = 0
        seen = set()

        while i < n-2:
            l = i + 1
            r = n -1
            
            while l < r:
                curr_sum = nums[i] + nums[l] + nums[r]
                if curr_sum == 0 and (nums[i], nums[l], nums[r]) not in seen:
                    res.append([nums[i], nums[l], nums[r]])
                    seen.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif curr_sum > 0:
                    r -= 1
                else:
                    l += 1
            i += 1
            while i < n and nums[i] == nums[i-1]:
                i += 1
        return res


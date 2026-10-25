class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        
        res = []

        l, r = 0, len(numbers) - 1

        while l <= r:
            curr_sum = numbers[l] + numbers[r]
            # print(l, r, curr_sum)
            if curr_sum == target:
                res.extend([l+1, r+1])
                return res
            elif curr_sum > target:
                r -= 1
            else:
                l += 1

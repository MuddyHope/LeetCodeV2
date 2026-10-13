from itertools import permutations

class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:
        
        temp = [bin(num)[2:] for num in nums]
        res = 0

        for p in permutations(temp):
            t_res = int("".join(p), 2)

            res = max(res, t_res)
        return res
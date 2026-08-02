class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        left_sum = [0] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            # 1 2 3 4
            left_sum[i] = prefix
            prefix *= nums[i]
        
        right_sum = [0] * len(nums)
        postfix = 1
        # print(f"leftsum: {left_sum}")

        for i in range(len(nums)-1, -1, -1):
            # print(f"i: {i}")
            res[i] = postfix * left_sum[i]
            right_sum[i] = postfix
            postfix *= nums[i]
            # print(f"right_sum[i]: {right_sum[i]}, postfix: {postfix}")
        
        return res
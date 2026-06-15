class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        ans = [1] * len(nums)
        left_prefix = [1] * len(nums)
        right_postfix = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            left_prefix[i] =(prefix)
            prefix *= nums[i]

        print(left_prefix)

        postfix = 1
        for j in range(len(nums)-1, -1, -1):
            right_postfix[j] = postfix
            ans[j] = postfix * left_prefix[j]
            postfix *= nums[j]
        print(right_postfix)

        return ans
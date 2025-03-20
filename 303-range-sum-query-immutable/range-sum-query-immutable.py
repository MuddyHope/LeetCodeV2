class NumArray:

    def __init__(self, nums: List[int]):
        self.sum_arry = []
        prefix = 0
        for i in range(len(nums)):
            prefix += nums[i]
            self.sum_arry.append(prefix)

    def sumRange(self, left: int, right: int) -> int:
        right_most = self.sum_arry[right]
        left_most = self.sum_arry[left-1] if left > 0 else 0
        return right_most - left_most


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
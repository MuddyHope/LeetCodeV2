from collections import Counter

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        counter = Counter(nums)

        j = 0
        for i in range(3):
            count = counter.get(i, 0)
            nums[j:j+count] = [i] * count
            j += count
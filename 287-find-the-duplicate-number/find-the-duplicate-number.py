class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        counter = set()
        for i in nums:
            if i in counter:
                return i
            else:
                counter.add(i)
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()

        for each in nums:
            if each in seen:
                return each
            else:
                seen.add(each)


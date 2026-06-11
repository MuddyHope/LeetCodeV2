class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for i in range(len(nums)):
            if target - nums[i] in hash_map:
                return [i, hash_map.get(target-nums[i])]
            hash_map[nums[i]] = i
        
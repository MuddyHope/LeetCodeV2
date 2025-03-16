class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}
        
        for each in range(len(nums)):
            if target - nums[each] in my_dict.keys():
                return [each, my_dict[target-nums[each]]]
            else:
                my_dict[nums[each]] = each
        return []
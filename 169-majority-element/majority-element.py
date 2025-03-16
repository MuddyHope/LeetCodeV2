class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # brute force method
        hash_map = {}
        curr_max = [0, 0]
        # number, times
        for i in range(len(nums)):
            if nums[i] in hash_map:
                hash_map[nums[i]] += 1
            else:
                hash_map[nums[i]] = 1
            if curr_max[1] < hash_map[nums[i]]:
                    curr_max[0] = nums[i]
                    curr_max[1] = i
        return curr_max[0]
        
            

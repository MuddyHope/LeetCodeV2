class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # brute force method
        max_count = len(nums)
        res = set()
        # use hash-map and list
        hash_map = {}
        for each_num in nums:
            hash_map[each_num] = hash_map.get(each_num, 0) + 1
            if hash_map[each_num] > max_count//3:
                    res.add(each_num)
        return list(res)

        
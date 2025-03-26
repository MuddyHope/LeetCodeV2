class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # brute force method
        max_count = len(nums)
        res = set()
        # use hash-map and list
        hash_map = {}
        for each_num in nums:
            if each_num in hash_map:
                hash_map[each_num] += 1
            else:
                hash_map[each_num] = 1
            if hash_map[each_num] > max_count//3:
                    res.add(each_num)
        return list(res)

        
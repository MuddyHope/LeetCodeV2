class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # brute force method
        max_count = len(nums)
        res = []
        # use hash-map and list
        hash_map = {}
        for each_num in nums:
            hash_map[each_num] = hash_map.get(each_num, 0) + 1
            if hash_map[each_num] > max_count//3 and each_num not in res:
                    res.append(each_num)
        return res

        
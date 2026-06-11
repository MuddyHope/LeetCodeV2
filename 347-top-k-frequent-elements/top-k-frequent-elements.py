class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # run through the list, make a dictionary, sort them based off of values, convert them into a list and show [:k]

        hash_map = {}

        for i in nums:
            hash_map[i] = hash_map.get(i, 0) + 1

        new_list = sorted(hash_map.keys(), key=lambda x: hash_map[x], reverse=True)
        return new_list[:k]
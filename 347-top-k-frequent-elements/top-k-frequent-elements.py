class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = Counter(nums)
        
        my_res = sorted(my_dict.keys(), key=lambda x: my_dict[x], reverse=True)[:k]
        return my_res

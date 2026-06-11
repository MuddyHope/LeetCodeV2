class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort

        freq = Counter(nums)

        buckets = [ [] for _ in range(len(nums) + 1)]

        for num, count in freq.items():
            buckets[count].append(num)
        
        res = []
        for each in range(len(buckets)-1, 0, -1):
            for num in buckets[each]:
                res.append(num)
        return res[:k]

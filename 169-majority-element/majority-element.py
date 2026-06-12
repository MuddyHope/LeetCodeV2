class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        # bucket sort

        buckets = [[] for _ in range(len(nums) + 1)]
        counter = Counter(nums)

        for num, count in counter.items():
            buckets[count].append(num)
        
        # print(buckets)

        # loop in reverse
        for num in reversed(range(len(buckets))):
            if buckets[num]:
                return buckets[num][0]
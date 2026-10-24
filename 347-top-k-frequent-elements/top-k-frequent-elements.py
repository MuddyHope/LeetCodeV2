class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        
        counter = Counter(nums)

        hq = []
        for _vk, v in counter.items():
            heapq.heappush(hq, (-v, _vk))
        

        print(hq[:k-1])

        # res = []

        # for _ in hq[:k-1]:
        #     res.append((_[1]))
        # return res
        i = 0
        res = []
        while i <= k:
            _v, _k = heapq.heappop(hq)
            res.append(_k)
            # print(f"_v, _k: {_v, _k}, i: {i}, res: {res}")

            i += 1
            if len(res) == k:
                return res
        return res

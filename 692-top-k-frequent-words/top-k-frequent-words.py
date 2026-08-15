class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        heap = []
        for val, count in counter.items():
            heapq.heappush(heap, (-count, val))
        res = []
        for _ in range(k):
            c, v = heapq.heappop(heap)
            res.append(v)
        return res
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = defaultdict(list)

        for start, end, time in times:
            graph[start].append((end, time))
        
        dist = {}
        heap = [(0, k)]

        while heap:
            time, node = heapq.heappop(heap)

            if node in dist:
                continue
            dist[node] = time

            for nei, _time in graph[node]:
                if nei not in dist:
                    heapq.heappush(heap, (time + _time, nei))
        return max(dist.values()) if len(dist) == n else -1
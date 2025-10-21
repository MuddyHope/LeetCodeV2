from collections import defaultdict
import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        

        # lets go through with prims algorithm

        N = len(points)
        adj = defaultdict(list)

        for i in range(N):
            x1, y1 = points[i]
            for j in range(i+1, N):
                x2, y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                adj[i].append((dist, j))
                adj[j].append((dist, i))


        minHeap = [(0,0)]
        visited = set()
        res = 0
        while len(visited) < N:
            dist, i = heapq.heappop(minHeap)
            if i in visited:
                continue
            visited.add(i)
            res += dist
            for nei_dist, nei in adj[i]:
                heapq.heappush(minHeap, (nei_dist, nei))
        
        return res
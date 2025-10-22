from collections import defaultdict
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        # Build adjacency list: src -> [(cost, dest)]
        adj = defaultdict(list)
        for each in flights:
            adj[each[0]].append((each[2], each[1]))

        # Heap stores: (total_price_so_far, current_city, stops)
        minHeap = [(0, src, 0)]

        # Use a visited dictionary to track the least stops used to reach each city
        visited = dict()

        while minHeap:
            price, node, stops = heapq.heappop(minHeap)

            # If destination reached within allowed stops, return price
            if node == dst:
                return price

            # If we've made more stops than allowed, skip
            if stops > k:
                continue

            # Avoid revisiting same node with more or equal stops
            if node in visited and visited[node] < stops:
                continue
            visited[node] = stops

            # Explore neighbors
            for cost, neighbor in adj[node]:
                heapq.heappush(minHeap, (price + cost, neighbor, stops + 1))
            # print(visited)

        return -1
            
                
        
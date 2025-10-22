import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        minHeap = [(grid[0][0], 0, 0)]

        directions = [[0,1], [1,0], [0,-1], [-1,0]]
        visited = set()
        while minHeap:
            time, x, y = heapq.heappop(minHeap)
            print(f"current: {x, y}, time: {time}")
            if (x,y) == (n-1, n-1):
                return time
            
            if (x,y) in visited:
                continue
            
            visited.add((x,y))

            for each_direction in directions:
                nx, ny = x+each_direction[0], y + each_direction[1]
                if 0 <= nx < n and 0 <= ny < n and (nx,ny) not in visited:
                    nxt_time = max(time, grid[nx][ny])
                    heapq.heappush(minHeap, (nxt_time, nx, ny))
            





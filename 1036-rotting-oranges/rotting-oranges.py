import collections
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        directions = [[0,-1], [0,1], [1,0], [-1,0]]
        seen = set()

        max_rows = len(grid)
        max_cols = len(grid[0])
        timer = 0

        def bfs(queue):
            nonlocal timer
            while queue:
                size = len(queue)
                print(f"queue: {queue}")
                for _ in range(size):
                    curr_x, curr_y = queue.popleft()
                    seen.add((curr_x, curr_y))

                    for dx, dy in directions:
                        nx, ny = curr_x + dx, curr_y + dy
                        if not (0 <= nx < max_rows and 0 <= ny < max_cols):
                            continue
                        if (nx, ny) in seen:
                            continue
                        if grid[nx][ny] == 1:
                            grid[nx][ny] = 2  # rot it
                            queue.append((nx, ny))
                            seen.add((nx, ny))
                if queue:  # only increment when new oranges rot
                    timer += 1

        # collect all rotten oranges and call bfs ONCE
        dq = collections.deque()
        for row in range(max_rows):
            for col in range(max_cols):
                if grid[row][col] == 2:
                    dq.append((row, col))
                    seen.add((row, col))
        print(f'Start DQ: {dq}')

        bfs(dq)

        # check if fresh oranges remain
        for row in range(max_rows):
            for col in range(max_cols):
                if grid[row][col] == 1:
                    return -1

        return timer

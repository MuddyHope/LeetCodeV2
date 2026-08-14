class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        p_oc = set()
        at_oc = set()

        rows = len(heights)
        cols = len(heights[0])

        # Pacific: top row + left column
        for r in range(rows):
            p_oc.add((r, 0))

        for c in range(cols):
            p_oc.add((0, c))

        # Atlantic: bottom row + right column
        for r in range(rows):
            at_oc.add((r, cols - 1))

        for c in range(cols):
            at_oc.add((rows - 1, c))

        
        # all the points from pacific ocean should flow 

        def bfs(starts):
            visited = set(starts)
            q = deque(starts)

            while q:
                r, c = q.popleft()

                for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                    nr = r + dr
                    nc = c + dc

                    if 0 <= nr < rows and 0 <= nc < cols:
                        
                        # Reverse water flow
                        if (nr, nc) not in visited and heights[nr][nc] >= heights[r][c]:
                            visited.add((nr, nc))
                            q.append((nr, nc))

            return visited

        pacific_reachable = bfs(p_oc)
        atlantic_reachable = bfs(at_oc)
        both = pacific_reachable & atlantic_reachable

        return list(both)

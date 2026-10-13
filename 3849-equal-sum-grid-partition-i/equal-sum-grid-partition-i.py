class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:

        m = len(grid)
        n = len(grid[0])

        total = 0

        for r in range(m):
            for c in range(n):
                total += grid[r][c]

        # Horizontal cuts
        res1 = 0

        for r in range(m - 1):
            for c in range(n):
                res1 += grid[r][c]

            res2 = total - res1

            if res1 == res2:
                return True

        # Vertical cuts
        res3 = 0

        for c in range(n - 1):
            for r in range(m):
                res3 += grid[r][c]

            res4 = total - res3

            if res3 == res4:
                return True

        return False
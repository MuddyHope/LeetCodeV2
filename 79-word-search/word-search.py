from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        seen = set()
        found = False

        def dfs(i, j, k):
            nonlocal found
            if found:   # early stop if already found
                return

            # check bounds
            if not (0 <= i < rows and 0 <= j < cols):
                return

            # check match
            if board[i][j] != word[k]:
                return

            # if last char matches, word found
            if k == len(word) - 1:
                found = True
                return

            seen.add((i, j))
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if (ni, nj) not in seen:
                    dfs(ni, nj, k + 1)
            seen.remove((i, j))

        # try every cell as a starting point
        for i in range(rows):
            for j in range(cols):
                dfs(i, j, 0)
                if found:
                    return True
        return False

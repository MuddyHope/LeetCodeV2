from typing import List
from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return

        ROWS, COLS = len(board), len(board[0])
        my_set = set()

        # Step 1: Collect border 'O's
        for r in range(ROWS):
            if board[r][0] == "O":
                my_set.add((r, 0))
            if board[r][COLS - 1] == "O":
                my_set.add((r, COLS - 1))

        for c in range(COLS):
            if board[0][c] == "O":
                my_set.add((0, c))
            if board[ROWS - 1][c] == "O":
                my_set.add((ROWS - 1, c))

        # Step 2: BFS to mark safe 'O's
        def bfs(r, c):
            q = deque([(r, c)])
            while q:
                cr, cc = q.popleft()
                if 0 <= cr < ROWS and 0 <= cc < COLS and board[cr][cc] == "O":
                    board[cr][cc] = "S"  # Mark safe
                    # explore neighbors
                    q.append((cr + 1, cc))
                    q.append((cr - 1, cc))
                    q.append((cr, cc + 1))
                    q.append((cr, cc - 1))

        for r, c in my_set:
            bfs(r, c)

        # Step 3: Flip all 'O' to 'X' (captured), and 'S' back to 'O' (safe)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "S":
                    board[r][c] = "O"

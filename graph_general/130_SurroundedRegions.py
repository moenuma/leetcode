class Solution:
    # capture surrounded regions
    # Time: O(m*n)
    # Space: O(m*n)
    def solve1(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        visited = set()

        def bfs(r, c):
            queue = deque()
            queue.append((r, c))
            visited.add((r, c))
            cur = set()
            cur.add((r, c))
            canFlip = True

            while queue:
                row, col = queue.popleft()
                directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

                for dr, dc in directions:
                    r = dr + row
                    c = dc + col
                    if r not in range(rows) or c not in range(cols):
                        canFlip = False
                    elif board[r][c] == "O" and (r, c) not in cur:
                        cur.add((r, c))
                        visited.add((r, c))
                        queue.append((r, c))
            if canFlip:
                for r, c in cur:
                    board[r][c] = "X"

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r, c) not in visited:
                    bfs(r, c)
    
    # capture everything except unsurrounded regions
    # Time: O(m*n)
    # Space: O(1)
    def solve2(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])

        def capture(r, c):
            if r not in range(rows) or c not in range(cols) or board[r][c] != "O":
                return
            board[r][c] = "T"
            capture(r+1, c)
            capture(r-1, c)
            capture(r, c+1)
            capture(r, c-1)

        # 1. (DFS) capture unsurrounded region (O -> T)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r in [0, rows-1] or c in [0, cols-1]):
                    capture(r, c)

        # 2. capture surrounded region (O -> X)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"

        # 3. uncapture unsurrounded region (T -> O)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "T":
                    board[r][c] = "O"
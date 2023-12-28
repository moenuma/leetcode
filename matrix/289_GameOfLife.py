class Solution:
    # Time: O(m*n)
    # Space: O(1)
    def gameOfLife(self, board: List[List[int]]) -> None:
        # Table:
        # Original | Now | State
        #    0     |  0  |   0
        #    1     |  0  |   1
        #    0     |  1  |   2
        #    1     |  1  |   3

        ROWS, COLS = len(board), len(board[0])

        def countNeighbors(r, c):
            nei = 0
            for i in range(r - 1, r + 2):
                for j in range(c - 1, c + 2):
                    if ((i == r and j == c) or i < 0 or j < 0 or i == ROWS or j == COLS):
                        continue
                    if board[i][j] in [1, 3]:
                        nei += 1
            return nei

        for row in range(ROWS):
            for col in range(COLS):
                nei = countNeighbors(row, col)

                if board[row][col]:
                    if nei in [2, 3]:
                        board[row][col] = 3
                
                elif nei == 3:
                    board[row][col] = 2
        
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == 1:
                    board[row][col] = 0
                elif board[row][col] in [2, 3]:
                    board[row][col] = 1
class Solution:
    # m: number of rows, n: number of columns
    # Calculate top to bottom (more complicated)
    # Time: O(m*n)
    # Space: O(m*n)
    def minPathSum1(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[0]*n for _ in range(m)]

        for row in range(m):
            for col in range(n):
                dp[row][col] = grid[row][col]
                if row-1 >= 0 and col-1 >= 0:
                    dp[row][col] += min(dp[row-1][col], dp[row][col-1])
                elif row-1 >= 0:
                    dp[row][col] += dp[row-1][col]
                elif col-1 >= 0:
                    dp[row][col] += dp[row][col-1]
        
        return dp[m-1][n-1]

    # Calculate bottom to top (simple)
    # Time: O(m*n)
    # Space: O(m*n)
    def minPathSum2(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dp = [[float("inf")]*(COLS+1) for _ in range(ROWS+1)]
        dp[ROWS-1][COLS] = 0

        for row in range(ROWS-1, -1, -1):
            for col in range(COLS-1, -1, -1):
                dp[row][col] = grid[row][col] + min(dp[row+1][col], dp[row][col+1])

        return dp[0][0]
    
    # Time: O(m*n)
    # Space: O(n)
    def minPathSum3(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dp = [float("inf")] * (COLS+1)
        dp[COLS-1] = 0

        for row in range(ROWS-1, -1, -1):
            for col in range(COLS-1, -1, -1):
                dp[col] = grid[row][col] + min(dp[col], dp[col+1])
                
        return dp[0]
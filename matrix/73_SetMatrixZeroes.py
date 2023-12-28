class Solution:
    # Time: O(m*n)
    # Space: O(m+n)
    def setZeroes1(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        # Find zeroes
        rows, cols = set(), set()
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    cols.add(col)
                    rows.add(row)
        
        for row in range(m):
            for col in range(n):
                if row in rows or col in cols:
                    matrix[row][col] = 0

    # Time: O(m*n)
    # Space: O(1)
    def setZeroes2(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        rowZero = False

        # check which rows/cols need to be zero
        for row in range(ROWS):
            for col in range(COLS):
                if matrix[row][col] == 0:
                    matrix[0][col] = 0

                    if row > 0:
                        matrix[row][0] = 0
                    else:
                        rowZero = True

        for row in range(1, ROWS):
            for col in range(1. COLS):
                if matrix[0][col] == 0 or matrix[row][0] == 0:
                    matrix[row][col] = 0
        
        if matrix[0][0] == 0:
            for row in range(ROWS):
                matrix[row][0] = 0
        
        if rowZero:
            for col in range(COLS):
                matrix[0][col] = 0
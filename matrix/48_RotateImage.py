class Solution:
    # Time: O(n^2)
    # Space: O(1)
    def rotate1(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        r = n - 1
        l = 0

        while l < r:
            for i in range(r-l):
                # top left to top right
                temp = matrix[i+l][r]
                matrix[i+l][r] = matrix[l][i+l]
                
                # top right to bottom right
                temp, matrix[r][r-i] = matrix[r][r-i], temp

                # bottom right to bottom left
                temp, matrix[r-i][l] = matrix[r-i][l], temp

                # bottom left to top left
                matrix[l][i+l] = temp
            
            r -= 1
            l += 1
    
    # Less temporary variables by rotating in a reverse order
    # Time: O(n^2)
    # Space: O(1)
    def rotate2(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix) - 1

        while l < r:
            for i in range(r - l):
                top, bottom = l, r

                # Save the top left
                topLeft = matrix[top][l + i]

                # Move bottom left into top left
                matrix[top][l + i] = matrix[bottom - i][l]

                # Move bottom right into bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]

                # Move top right into bottom right
                matrix[bottom][r - i] = matrix[top + i][r]

                # Move top left into top right
                matrix[top + i][r] = topLeft

            l += 1
            r -= 1
    
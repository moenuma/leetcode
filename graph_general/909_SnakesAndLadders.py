class Solution:
    # Time: O(n^2)
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        board.reverse()

        def squareToPos(square):
            row = (square - 1) // n
            col = (square - 1) % n
            if row % 2 == 1:
                col = (n - 1) - col
            return [row, col]

        queue = deque() # [square, move]
        queue.append([1, 0])
        visit = set()

        while queue:
            curSquare, curMove = queue.popleft()

            for i in range(1, 7):
                nextSquare = curSquare + i
                row, col = squareToPos(nextSquare)
                if board[row][col] != -1:
                    nextSquare = board[row][col]
                if nextSquare == n**2:
                    return curMove + 1
                if nextSquare not in visit:
                    visit.add(nextSquare)
                    queue.append([nextSquare, curMove+1])
            
        return -1
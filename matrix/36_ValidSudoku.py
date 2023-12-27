class Solution:
    # Time: O(9^2)
    def isValidSudoku1(self, board: List[List[str]]) -> bool:
        cols = {}
        subboxes = {}

        for r in range(len(board)):
            rows = set()
            for c in range(len(board[r])):
                cell = board[r][c]
                pos = (r // 3) * 3 + c // 3
                if cell == ".":
                    continue
                if cell in rows or 
                    (c in cols and cell in cols[c]) or
                    (pos in subboxes and cell in subboxes[pos]):
                    return False
                
                rows.add(cell)
                if c not in cols:
                    cols[c] = set(cell)
                else:
                    cols[c].add(cell)
                if pos not in subboxes:
                    subboxes[pos] = set(cell)
                else:
                    subboxes[pos].add(cell)
        
        return True 
    
    # initialize cols and subboxes dictionary
    def isValidSudoku2(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        subboxes = collections.defaultdict(set)

        for r in range(len(board)):
            rows = set()
            for c in range(len(board[r])):
                cell = board[r][c]
                pos = (r // 3) * 3 + c // 3
                if cell == ".":
                    continue
                if cell in rows or cell in cols[c] or cell in subboxes[pos]:
                    return False
                
                rows.add(cell)
                cols[c].add(cell)
                subboxes[pos].add(cell)
        
        return True 
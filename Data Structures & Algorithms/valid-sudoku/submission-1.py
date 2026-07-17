from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])
        row_check = defaultdict(set) # row number -> set()
        col_check = defaultdict(set) # col number
        box_check = defaultdict(set) # tuple (r,c) wher (0,0) is top left box
        for r in range(rows):
            for c in range(cols):
                value = board[r][c]
                if value == ".":
                    continue
                box = (r // 3, c // 3)
                if (
                    value in row_check[r] or 
                    value in col_check[c] or
                    value in box_check[box]
                ):
                    return False
                row_check[r].add(value)
                col_check[c].add(value)
                box_check[box].add(value)
        return True
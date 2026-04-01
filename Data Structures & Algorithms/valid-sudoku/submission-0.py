class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == '.': continue

                num = board[r][c]
                row_info = ('row', r, num)
                col_info = ('col', c, num)
                box_info = ('box', r//3, c//3, num)

                if row_info in seen or col_info in seen or box_info in seen:
                    return False

                seen.add(row_info)
                seen.add(col_info)
                seen.add(box_info)

        return True

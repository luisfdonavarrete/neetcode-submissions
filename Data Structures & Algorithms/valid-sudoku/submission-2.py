class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols, boxes = defaultdict(set), defaultdict(set), defaultdict(set)
        
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in rows[i]:
                        return False
                    rows[i].add(board[i][j])

                    if board[i][j] in boxes[f"{int(i/3)}{int(j/3)}"]:
                        return False
                    boxes[f"{int(i/3)}{int(j/3)}"].add(board[i][j])

                if board[j][i] != '.':
                    if board[j][i] in cols[i]:
                        return False
                    cols[i].add(board[j][i])

        return True
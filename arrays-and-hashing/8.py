from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool: # type: ignore
        rowCheck = defaultdict(set) 
        colCheck = defaultdict(set)
        boxCheck = defaultdict(set)
        
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in rowCheck[i] or board[i][j] in colCheck[j] or board[i][j] in boxCheck[(i // 3, j // 3)]:
                    return False
                else:
                    rowCheck[i].add(board[i][j])
                    colCheck[j].add(board[i][j])
                    boxCheck[(i // 3, j // 3)].add(board[i][j])

        return True
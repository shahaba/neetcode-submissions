class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def checkrow(row):
            seen = set()
            print("Checking value: ", board[row])
            for i in range(0, 9):
                if board[row][i] == ".":
                    continue
                elif board[row][i] not in seen:
                    seen.add(board[row][i])
                else:
                    return False
            print("values in row: ", seen)
            return True
        
        def checkcol(col):
            seen = set()
            for i in range(0, 9):
                if board[i][col] == ".":
                    continue
                elif board[i][col] not in seen:
                    seen.add(board[i][col])
                else:
                    return False
            print("values in col: ", seen)
            return True

        def checkgrid(row, col):
            seen = set()
            for i in range(row, row+3):
                for j in range(col, col+3):
                    if board[i][j] == ".":
                        continue
                    elif board[i][j] not in seen:
                        seen.add(board[i][j])
                    else:
                        print("seen already")
                        return False
            print("values in grid: ", seen)
            return True

        # check 1d
        for i in range(9):
            if not checkrow(i):
                return False
            if not checkcol(i):
                return False

        # check 2d
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not checkgrid(i, j):
                    return False
        
        return True

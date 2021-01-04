class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        self.board = board
        self.solver()
        
        
    def solver(self):
        i, j = self.findNext()
        if i == -1: return True# board is full
        
        for value in range(1, 10): #[1, 9]
            if self.choiceIsValid(i, j, str(value)):
                self.board[i][j] = str(value)
                if self.solver():
                    return True
                # recursive backtrack, un-set the value
                self.board[i][j] = "."
        
        return False
        

            
    # find next empty location
    # return (-1, -1) if board is full
    def findNext(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == ".":
                    return i,j
            
        return -1, -1
        
    # check if put a new value at index (i, j) keeps the new Sudoku Valid
    def choiceIsValid(self, i, j, value):
        rowValid = all(value != self.board[i][k] for k in range(9))
        if rowValid:
            columnValid = all(value != self.board[k][j] for k in range(9))
            if columnValid:
                # top corner = (topX, topY)
                topX, topY = i//3*3, j//3*3
                
                # box valid
                for x in range(topX, topX+3):
                    for y in range(topY, topY+3):
                        if self.board[x][y] == value: return False
                
                return True
        
        return False
        
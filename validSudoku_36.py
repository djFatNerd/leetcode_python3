class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[0]*9 for i in range(9)]
        columns = [[0]*9 for i in range(9)]
        boxes = [[0]*9 for i in range(9)]
        
        for i in range(9): # row# 
            for j in range(9): # column#
                box_num = (i // 3) * 3 + j // 3
                if board[i][j] != '.':
                    num = int(board[i][j]) - 1 # 1-9 -> 0-8
                    if rows[i][num] == 1 or columns[j][num] == 1 or boxes[box_num][num] == 1:return False
                    rows[i][num] = 1
                    columns[j][num] = 1
                    boxes[box_num][num] = 1
        
        return True
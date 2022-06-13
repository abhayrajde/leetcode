class Solution(object):
    def isValidSudoku(self, board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                
                if(board[i][j]!="."):
                    # TO VALIDATE THE SUDOKU 3 MAIN STEPS

                    # 1. CHECK THE ROW
                    for x in range(len(board[0])):
                        if(board[i][x]==board[i][j] and x!=j):
                            return(False)

                    # 2. CHECK THE COLUMN
                    for y in range(len(board)):
                        if(board[y][j] == board[i][j] and y!=i):
                            return(False)

                    # 3. CHECK THE BOX OF 3*3
                    x_box = i//3
                    y_box = j//3
                    for x in range(x_box*3,(x_box*3)+3):
                        for y in range(y_box*3,(y_box*3)+3):
                            if(board[x][y]==board[i][j] and x!=i and y!=j):
                                return(False)
        return(True)

                    
                    
                    

        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
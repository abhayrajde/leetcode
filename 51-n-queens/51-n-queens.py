class Solution(object):
    def solveNQueens(self, n):
        self.n = n
        res = []
        
        # CREATING THE BOARD NXN
        board = []
        for i in range(n):
            temp = []
            for j in range(n):
                temp.append(".")
            board.append(temp)
        
        self.solve(board,0,res)
        return(res)
        
    def solve(self,board,col,res):
        if(col == self.n):
            temp1 = []
            for i in range(self.n):
                temp2 = ""
                for j in range(self.n):
                    temp2+=board[i][j]
                temp1.append(temp2)
            res.append(temp1)
            return(True)
        
        for i in range(self.n):
            position = (i,col)
            
            if(self.validate(board,position)):
                board[position[0]][position[1]] = "Q"
                
                if(self.solve(board,col+1,res)):
                    pass
                    # return(True)
            
            board[position[0]][position[1]] = "."
        return(False)
    
    
    def validate(self,board, pos):
        # CHECK SAME ROW - BUT WE HAD TOOK CARE OF THAT
        for i in range(len(board[0])):
            if(board[pos[0]][i] != "." and i != pos[1]):
                return(False)

        # CHECK SAME COLUMN
        for i in range(len(board)):
            if(board[i][pos[1]] != "." and i != pos[0]):
                return(False)

        # INITIALIZING I AND J WILL BE DONE SEPERATELY FOR ALL THE WHILE LOOPS DOWN
        i = pos[0] - 1
        j = pos[1] - 1

        # CHECK LEFT-UP
        while(i>=0 and j>=0):
            if(board[i][j] != "."):
                return(False)
            i -= 1
            j -= 1

        i = pos[0] + 1
        j = pos[1] - 1
        
        # CHECK LEFT-DOWN
        while(i<=self.n-1 and j>=0):
            if(board[i][j] != "."):
                return(False)
            i += 1
            j -= 1

        i = pos[0] - 1
        j = pos[1] + 1
        
        # CHECK RIGHT-UP
        while(i>=0 and j<=self.n-1):
            if(board[i][j] != "."):
                return(False)
            i -= 1
            j += 1

        i = pos[0] + 1
        j = pos[1] + 1
        
        # CHECK RIGHT-DOWN
        while(i<=self.n-1 and j<=self.n-1):
            if(board[i][j] != "."):
                return(False)
            i += 1
            j += 1

        return(True)

        
        """
        :type n: int
        :rtype: List[List[str]]
        """
        
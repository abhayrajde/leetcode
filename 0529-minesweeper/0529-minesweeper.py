class Solution(object):
    def get_adjecent_mines(self,board,x,y):
        num_mines = 0
        
        for r in range(x-1,x+2):
            for c in range(y-1,y+2):
                if(r>=0 and r<len(board) and c>=0 and c<len(board[0]) and board[r][c] == "M"):
                    num_mines+=1
        return num_mines
    
    def updateBoard(self, board, click):
        #check for valid board
        if not board:
            return board
        
        x,y = click
        
        if board[x][y] == "M":
            board[x][y] = "X"
        else:
            num_mines = self.get_adjecent_mines(board, x, y)
            if num_mines:
                board[x][y] = str(num_mines)
            else:
                board[x][y] = "B"
                for r in range(x-1,x+2):
                    for c in range(y-1,y+2):
                        if(r>=0 and r<len(board) and c>=0 and c<len(board[0]) and board[r][c] != "B"):
                            self.updateBoard(board,[r,c])
                
        return board
        
        
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        
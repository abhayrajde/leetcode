class Solution(object):
    def solve(self, board):
        # STEP 1: CAPTURE UNSURROUNDED REGION- AND BY APPLYING DFS CONVERT ALL ELEMENTS INTO 'T'
        rows, cols = len(board), len(board[0])
        # visited = 
        def dfs(r,c):
            if(r<0 or c<0 or
              r == rows or c == cols or
              board[r][c] == "T" or board[r][c] == "X"):
                return
            board[r][c] = "T"
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        
        # VERTICAL TRAVERSAL
        for r in range(rows):
            if(board[r][0] == "O"):
                dfs(r,0)
            if(board[r][cols-1] == "O"):
                dfs(r,cols-1)
                
        # HORIZONTAL TRAVERSAL
        for c in range(cols):
            if(board[0][c] == "O"):
                dfs(0,c)
            if(board[rows-1][c] == "O"):
                dfs(rows-1,c)
                
        
        #2. CAPTURE SURROUNDED REGIONS - CONVERT THEM TO 'X'
        for r in range(rows):
            for c in range(cols):
                if(board[r][c] == "O"):
                    board[r][c] = "X"
        
        
        #3. CONVERT THE UNSURROUNDED REGIONS FROM 'T' TO 'O'
        for r in range(rows):
            for c in range(cols):
                if(board[r][c] == "T"):
                    board[r][c] = "O"
        
        
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        
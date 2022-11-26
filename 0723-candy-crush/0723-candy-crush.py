class Solution(object):
    def candyCrush(self, board):
        rows = len(board)
        cols = len(board[0])
        while True:
            # for i in board:
            #     print(i)    
            # print(next)
            # 1, Check
            crush = set()
            for r in range(rows):
                for c in range(cols):
                    if r < rows-2 and board[r][c] == board[r+1][c] == board[r+2][c] != 0:
                        crush.add((r,c))
                        crush.add((r+1,c))
                        crush.add((r+2,c))
                    if c < cols-2 and board[r][c] == board[r][c+1] == board[r][c+2] != 0:
                        crush.add((r,c))
                        crush.add((r,c+1))
                        crush.add((r,c+2))
            # 2, Crush
            if not crush: 
                break
            for r,c in crush: 
                board[r][c] = 0

            # 3, Drop
            
            for c in range(cols):
                count = 0
                col_ele = []
                for r in range(rows):
                    if board[r][c] != 0:
                        col_ele.append(board[r][c])
                    else:
                        count += 1
                for r in range(rows-1,-1,-1):
                    if col_ele:
                        board[r][c] = col_ele[-1]
                        col_ele.pop()
                    else:
                        board[r][c] = 0
                    
                    
        return board
        """
        :type board: List[List[int]]
        :rtype: List[List[int]]
        """
        
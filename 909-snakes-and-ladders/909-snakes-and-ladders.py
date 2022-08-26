class Solution(object):
    def snakesAndLadders(self, board):
        n = len(board[0])
        visited = set()
        board.reverse()
        def inttopos(square):
            r = (square-1)//n
            c = (square-1) % n
            if(r%2 == 1):
                c = n-1-c
            return [r,c]
        
        q = deque() #[square,moves]
        q.append([1,0])
        while q:
            square,moves = q.popleft()
            for i in range(1,7):
                nextsquare = square+i
                r,c = inttopos(nextsquare)
                if(board[r][c]!=-1):
                    nextsquare = board[r][c]
                if(nextsquare == (n*n)):
                    return moves+1
                if(nextsquare not in visited):
                    visited.add(nextsquare)
                    q.append([nextsquare,moves+1])
        return -1
        """
        :type board: List[List[int]]
        :rtype: int
        """
        
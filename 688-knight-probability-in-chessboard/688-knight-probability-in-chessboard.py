class Solution(object):
    def knightProbability(self, n, k, row, column):
        curr = [[0]*n for i in range(n)]
        nxt = [[0]*n for i in range(n)]
        
        curr[row][column] = 1.0
        
        moves = [(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1)]
        
        def validate(r,c):
            if(0 <= r < n and 0 <= c < n):
                return True
            return False
        
        for m in range(k):
            for r in range(n):
                for c in range(n):
                    if(curr[r][c]!=0):
                        for nr,nc in moves:
                            next_r = r + nr
                            next_c = c + nc
                            if validate(next_r,next_c):
                                nxt[next_r][next_c] += curr[r][c]/8.0
            curr = nxt
            nxt = [[0]*n for i in range(n)]
        
        res = 0.0
        for r in range(n):
            for c in range(n):
                res+=curr[r][c]
        return res
        """
        :type n: int
        :type k: int
        :type row: int
        :type column: int
        :rtype: float
        """
        
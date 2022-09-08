class Solution(object):
    def maximalSquare(self, matrix):
        rows, cols = len(matrix), len(matrix[0])
        cache = {}
        
        def helper(r,c):
            if r>=rows or c>=cols:
                return 0
            
            if (r,c) not in cache:
                down = helper(r+1,c)
                right = helper(r,c+1)
                diag = helper(r+1,c+1)
                cache[(r,c)] = 0
                if matrix[r][c] == "1":
                    cache[(r,c)] = 1 + min(down,right,diag)
                    
            return cache[(r,c)]
        helper(0,0)
        return(max(cache.values())**2)
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        
class Solution(object):
    def maxAreaOfIsland(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        
        visited = set()
        maxarea = 0
        
        def dfs(r, c):
            if( r < 0 or c < 0 or
              r == rows or c == cols or
              (r,c) in visited or grid[r][c] == 0):
                return 0
            visited.add((r,c))
            return(1 + dfs(r+1,c) +
                        dfs(r-1,c) +
                        dfs(r,c+1) +
                        dfs(r,c-1))
            
        for r in range(rows):
            for c in range(cols):
                maxarea = max(maxarea, dfs(r,c))
        return(maxarea)
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
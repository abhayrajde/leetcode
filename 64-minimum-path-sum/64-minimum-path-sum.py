class Solution(object):
    def minPathSum(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        dp = [[float("inf")]*(cols+1) for r in range(rows+1)]
        
        dp[rows][cols-1] = 0
        # print(dp)
        for r in range(rows-1,-1,-1):
            for c in range(cols-1,-1,-1):
                dp[r][c] = grid[r][c] + min(dp[r+1][c], dp[r][c+1])
        
        return(dp[0][0])
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
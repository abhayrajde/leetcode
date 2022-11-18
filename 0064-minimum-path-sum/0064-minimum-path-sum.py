class Solution(object):
    def minPathSum(self, grid):
        
        rows = len(grid)
        cols = len(grid[0])
        
        #Tabulation
        
#         dp = [[0]*cols]*rows
        
#         for r in range(rows):
#             for c in range(cols):
#                 if r == 0 and c == 0:
#                     dp[r][c] = grid[r][c]
#                 else:
#                     if r-1 >= 0:
#                         up = grid[r][c] + dp[r-1][c]
#                     else:
#                         up = float("inf")
#                     if c-1 >= 0:
#                         left = grid[r][c] + dp[r][c-1]
#                     else:
#                         left = float("inf")

#                     dp[r][c] = min(left,up)
#         return dp[rows-1][cols-1]
        
        #Memoization
        # dp = [[-1]*cols]*rows
        dp = [[-1 for x in range(cols)] for y in range(rows)]
        def dfs(i,j,dp):
            # print(dp)
            #Base Conditions
            if i == rows-1 and j == cols-1:
                dp[i][j] = grid[i][j]
                return grid[i][j]
            
            if i >= rows  or j >= cols:
                return float("inf")
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            down = grid[i][j] + dfs(i+1,j,dp)
            right = grid[i][j] + dfs(i,j+1,dp)
            
            dp[i][j] = min(down, right)
            
            return dp[i][j]
            
        return dfs(0,0,dp)
        print(dp)
        
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
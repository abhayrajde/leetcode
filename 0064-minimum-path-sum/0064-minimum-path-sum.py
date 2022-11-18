class Solution(object):
    def minPathSum(self, grid):
        
        rows = len(grid)
        cols = len(grid[0])
        
        #Tabulation
        
        dp = [[0]*cols]*rows
        
        for r in range(rows):
            for c in range(cols):
                if r == 0 and c == 0:
                    dp[r][c] = grid[r][c]
                else:
                    if r-1 >= 0:
                        up = grid[r][c] + dp[r-1][c]
                    else:
                        up = float("inf")
                    if c-1 >= 0:
                        left = grid[r][c] + dp[r][c-1]
                    else:
                        left = float("inf")

                    dp[r][c] = min(left,up)
        return dp[rows-1][cols-1]

        #         dp = [[-1]*cols]*rows
#         def dfs(i,j,dp):
#             # print(dp)
#             #Base Conditions
#             if i == 0 and j == 0:
#                 return grid[i][j]
            
#             if i < 0  or j < 0:
#                 return float("inf")
            
#             if dp[i][j] != -1:
#                 return dp[i][j]
            
#             up = grid[i][j] + dfs(i-1,j,dp)
#             left = grid[i][j] + dfs(i,j-1,dp)
            
#             dp[i][j] = min(up, left)
            
#             return dp[i][j]
            
#         return dfs(rows-1,cols-1,dp)
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
class Solution(object):
    def uniquePaths(self, m, n):
        dp = [[0 for j in range(n+1)]for i in range(m+1)]
        dp[m-1][n-1] = 1
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if(i == (m-1) and j == (n-1)):
                     dp[i][j] = 1
                else:
                    dp[i][j] = dp[i+1][j] + dp[i][j+1]
        return(dp[0][0])
                
                
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
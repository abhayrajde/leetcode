class Solution(object):
    def uniquePaths(self, m, n):
        
        dp = [[0]*n for i in range(m)]
        
        for r in range(m):
            for c in range(n):
                if r == 0 or c == 0:
                    dp[r][c] = 1
                else:
                    dp[r][c] = dp[r-1][c] + dp[r][c-1]
        return dp[m-1][n-1]
#         q = deque()
#         q.append((0,0))
#         visited = set((0,0))
#         count = 0
#         while (q):
#             for i in range(len(q)):
#                 currm, currn = q.popleft()
                
#                 if(currm == m-1 and currn == n-1):
#                     return c
#                 #Down
#                 if(currm+1 < m and (currm+1, currn) not in visited):
#                     q.append((currm+1,currn))
#                     visited.add((currm+1,currn))
#                     count+=1
                
#                 #RIGHT
#                 if(currn+1 < n and (currm, currn+1) not in visited):
#                     q.append((currm,currn+1))
#                     visited.add((currm,currn+1))
#                     count+=1
#         return count
        
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
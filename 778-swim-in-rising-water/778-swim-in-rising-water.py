class Solution(object):
    def swimInWater(self, grid):
        n = len(grid)
        visit = set()
        visit.add((0,0))
        minh = [[grid[0][0],0,0]]
        
        while minh:
            t,r,c = heapq.heappop(minh)
            
            if(r == n-1 and c == n-1):
                return t
            
            #Down
            if(r+1 < n and ((r+1,c) not in visit)):
                heapq.heappush(minh, [max(grid[r+1][c],t),r+1,c])
                visit.add((r+1,c))
            
            #Up
            if(r-1 >= 0 and ((r-1,c) not in visit)):
                heapq.heappush(minh, [max(grid[r-1][c],t),r-1,c])
                visit.add((r-1,c))
                
            #Right
            if(c+1 < n and ((r,c+1) not in visit)):
                heapq.heappush(minh, [max(grid[r][c+1],t),r,c+1])
                visit.add((r,c+1))
            
            #Left
            if(c-1 >= 0 and ((r,c-1) not in visit)):
                heapq.heappush(minh, [max(grid[r][c-1],t),r,c-1])
                visit.add((r,c-1))
            
                
                
            
        
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
'''
def rotten_next(grid,temp, queue, m, n, fresh):
        i = temp[0]
        j = temp[1]
       
        #up
        if(i-1 >= 0 and grid[i-1][j] == 1):
            queue.append((i-1,j))
            grid[i-1][j] = 2
            fresh -= 1
       
        #down
        if(i+1 < m and grid[i+1][j] == 1):
            queue.append((i+1,j))
            grid[i+1][j] = 2
            fresh -= 1
           
        #right
        if(j+1 < n and grid[i][j+1] == 1):
            queue.append((i,j+1))
            grid[i][j+1] = 2
            fresh -= 1
           
        #up
        if(j-1 >= 0 and grid[i][j-1] == 1):
            queue.append((i,j-1))
            grid[i][j-1] = 2
            fresh -= 1
'''      
           
class Solution(object):
           
           
    def orangesRotting(self, grid):
       
        queue = []
        time = 0
        fresh = 0
        m = len(grid)
        n = len(grid[0])
       
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j] == 1):
                    fresh += 1
                if(grid[i][j] == 2):
                    queue.append((i,j))
           
        while(len(queue) != 0 and fresh > 0 ):
            for i in range(len(queue)):
                temp = queue.pop(0)
                # rotten_next(grid,temp,queue, m, n,fresh)
                r = temp[0]
                c = temp[1]

                #up
                if(r-1 >= 0 and grid[r-1][c] == 1):
                    queue.append((r-1,c))
                    grid[r-1][c] = 2
                    fresh -= 1

                #down
                if(r+1 < m and grid[r+1][c] == 1):
                    queue.append((r+1,c))
                    grid[r+1][c] = 2
                    fresh -= 1

                #right
                if(c+1 < n and grid[r][c+1] == 1):
                    queue.append((r,c+1))
                    grid[r][c+1] = 2
                    fresh -= 1

                #left
                if(c-1 >= 0 and grid[r][c-1] == 1):
                    queue.append((r,c-1))
                    grid[r][c-1] = 2
                    fresh -= 1
               
               
               
            time += 1
        return (time if fresh == 0 else -1)
           
        """
        :type grid: List[List[int]]
        :rtype: int
        """
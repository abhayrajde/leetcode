class Solution(object):
    def numIslands(self, grid):
        if(not grid):
            return (0)
        
        rows,cols = len(grid), len(grid[0])
        visited = set()
        islands = 0
        
        def bfs(r,c):
            q = deque()
            visited.add((r,c))
            q.append((r,c))
            while q:
                row, col = q.popleft()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                for i,j in directions:
                    r = row+i
                    c = col+j
                    if(r in range(rows) and
                       c in range(cols) and
                       grid[r][c] == "1" and 
                       (r,c) not in visited):
                        q.append((r,c))
                        visited.add((r,c))
        for r in range(rows):
            for c in range(cols):
                if(grid[r][c]=="1" and ((r,c) not in visited)):
                    bfs(r,c)
                    islands+=1
        return(islands)
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
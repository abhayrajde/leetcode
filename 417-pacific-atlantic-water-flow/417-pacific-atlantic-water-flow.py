class Solution(object):
    def pacificAtlantic(self, heights):
        pac = set()
        atl = set()
        
        row,col = len(heights),len(heights[0])
        
        def dfs(r,c,visited,prevheight):
            if((r,c) in visited or
                r < 0 or c < 0 or
                r==row or c == col or
                heights[r][c] < prevheight):
                return
            visited.add((r,c))
            dfs(r+1,c,visited,heights[r][c])
            dfs(r-1,c,visited,heights[r][c])
            dfs(r,c+1,visited,heights[r][c])
            dfs(r,c-1,visited,heights[r][c])
        
        for c in range(col):
            dfs(0,c,pac,heights[0][c])
            dfs(row-1,c,atl,heights[row-1][c])
        
        for r in range(row):
            dfs(r,0,pac,heights[r][0])
            dfs(r,col-1,atl,heights[r][col-1])
        
        res = []
        for r in range(row):
            for c in range(col):
                if(((r,c) in pac) and ((r,c) in atl)):
                    res.append((r,c))
        return(res)
                    
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        
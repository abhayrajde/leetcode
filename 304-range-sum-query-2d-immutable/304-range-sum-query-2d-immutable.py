class NumMatrix(object):

    def __init__(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        self.summat = [[0]*(cols+1) for r in range(rows+1)]
        
        for r in range(rows):
            prefix = 0
            for c in range(cols):
                prefix += matrix[r][c] 
                above = self.summat[r][c+1]
                self.summat[r+1][c+1] = prefix+above
                
        """
        :type matrix: List[List[int]]
        """
        

    def sumRegion(self, row1, col1, row2, col2):
        r1 , c1 , r2 , c2 = row1+1, col1+1, row2+1, col2+1
        botright = self.summat[r2][c2]
        left = self.summat[r2][c1-1]
        above = self.summat[r1-1][c2]
        topleft = self.summat[r1-1][c1-1]
        
        return (botright - left - above + topleft)
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
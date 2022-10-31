class NumMatrix(object):

    def __init__(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        self.mat = matrix
        self.presum = [[0]*(cols+1) for r in range(rows+1)]
        
        # for r in range(rows):
        #     prefix = 0
        #     for c in range(cols):
        #         prefix += matrix[r][c] 
        #         above = self.presum[r][c+1]
        #         self.presum[r+1][c+1] = prefix+above
        
        """
        :type matrix: List[List[int]]
        """
    def generate_presum (self):
        rows = len(self.mat)
        cols = len(self.mat[0])
        self.presum = [[0]*(cols+1) for r in range(rows+1)]
        
        for r in range(rows):
            prefix = 0
            for c in range(cols):
                prefix += self.mat[r][c] 
                above = self.presum[r][c+1]
                self.presum[r+1][c+1] = prefix+above
        return self.presum
        
    def update(self, row, col, val):
        self.mat[row][col] = val
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: None
        """
        

    def sumRegion(self, row1, col1, row2, col2):
        self.presum = self.generate_presum()
        r1 , c1 , r2 , c2 = row1+1, col1+1, row2+1, col2+1
        botright = self.presum[r2][c2]
        left = self.presum[r2][c1-1]
        above = self.presum[r1-1][c2]
        topleft = self.presum[r1-1][c1-1]
        
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
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)
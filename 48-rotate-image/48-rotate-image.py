class Solution(object):
    def rotate(self, matrix):
        #STEP 1: TRANSPOSE OF THE MATRIX
        transposed = set()
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if((r,c) not in transposed):
                    matrix[r][c],matrix[c][r] = matrix[c][r],matrix[r][c]
                    # transpose.add((r,c))
                    transposed.add((c,r))
        
        #STEP 2: REVERSE THE MATRIX
        for r in matrix:
            r.reverse()
        # matrix.reverse()
        
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
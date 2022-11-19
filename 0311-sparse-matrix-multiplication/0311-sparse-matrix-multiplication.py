class Solution(object):
    def multiply(self, mat1, mat2):
        res = [[0] * len(mat2[0]) for i in range(len(mat1))]
        # res = [[0] for i in range(len(mat2[0])) for j in range (len(mat1))]
        
        for r in range(len(res)):
            for c in range(len(res[0])):
                
                for i in range(len(mat1[0])):
                    res[r][c] += (mat1[r][i] * mat2[i][c])
                    
        return res
    
    # def multiply(self, A, B):
    #     mA,nA,nB = len(A),len(A[0]),len(B[0])
    #     res = [[0]*len(B[0]) for _ in xrange(mA)]
    #     for i in xrange(mA):
    #         for j in xrange(nA):
    #             if A[i][j]:
    #                 for k in xrange(nB):
    #                     res[i][k] += A[i][j]*B[j][k]
    #     return res
        """
        :type mat1: List[List[int]]
        :type mat2: List[List[int]]
        :rtype: List[List[int]]
        """
        
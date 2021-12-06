import copy
class Solution(object):
    def setZeroes(self, matrix):
        
        # RUNTIME ERROR (AS EXPECTED :)
        listi = []
        listj = []
        matrix1 = copy.deepcopy(matrix)
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if (matrix[i][j] == 0):
                    listi.append(i)
                    listj.append(j)
                    
                    # a = i
                    # b = j
        for j in listj:
            # if((j not in listj)): #and(i not in listi)):
                # listj.append(j)
            for x in range(len(matrix)):
                matrix[x][j] = 0
            # if(i not in listi):
        for i in listi:
            
                #listi.append(i)
            for y in range(len(matrix[0])):
                matrix[i][y] = 0
        """"""
        """
        if returning the different matrix was allowed then this could be one of the solution
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if (matrix[i][j] == 0):
                    # a = i
                    # b = j
                    for x in range(len(matrix)):
                        matrix1[i][x] = 0
                    for y in range(len(matrix[0])):
                        matrix1[y][j] = 0
        print(matrix1)
    
        """
                        
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
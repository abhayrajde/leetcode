class Solution(object):
    def rotate(self, matrix):
        # FOR THIS SUM WE WILL TAKE THE APPROACH OF TRANSPOSE AND REVERSE
        # FIRST WE WILL DO THE TRANSPOSE OF THE MATRIX
        # THEN SECOND STEP WOULD BE DOING THE REVERSE OF ALL THE ROWS OF THE MATRIX
        list1 = []
        # STEP 1 : TRANSPOSE
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                
                temp = [i,j]
                if(temp not in list1):
                # temp = matrix[i][j]
                # matrix[i][j] = matrix[j][i]
                # matrix[j][i] = temp
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
                
                
                temp1 = [i,j]
                temp2 = [j,i]
                if(temp1 not in list1):
                    list1.append(temp1)
                    list1.append(temp2)
        # STEP 2 : REVERSE OF THE EACH ROWS IN THE MATRIX
        for i in range(len(matrix)):
            matrix[i].reverse()
            
        
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
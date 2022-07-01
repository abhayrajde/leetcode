class Solution(object):
    def spiralOrder(self, matrix):
        spiral = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
        
        # TO TRAVERSE THE MATRIX IN SPIRAL ORDER
        while(left < right and top < bottom):
            
            # 1: LEFT TO RIGHT TRAVERSAL --->
            for i in range(left,right):
                spiral.append(matrix[top][i])
            top+=1
            
            # 2: TOP TO BOTTOM
            for i in range(top, bottom):
                spiral.append(matrix[i][right-1])
            right-=1
            
            if not (left<right and top<bottom):
                break
            
            # 3: RIGHT TO LEFT   <----
            for i in range(right-1, left-1, -1):
                spiral.append(matrix[bottom - 1][i])
            bottom -= 1
            
            # 4: BOTTOM TO UP
            for i in range(bottom-1,top-1,-1):
                spiral.append(matrix[i][left])
            left += 1
        return(spiral)
            
            
        
        
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
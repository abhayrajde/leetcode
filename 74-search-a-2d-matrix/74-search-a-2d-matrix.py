class Solution(object):
    def searchMatrix(self, matrix, target):
        top = 0
        bottom = len(matrix) - 1
        
        while(top <= bottom):
            mid = (top + bottom) // 2
            if(target < matrix[mid][0]):
                bottom = mid - 1
            elif(target > matrix[mid][-1]):
                top = top + 1
            else:
                break
        
        if(not top <= bottom):
            return(False)
        mid = (top + bottom)//2
        low = 0
        high = len(matrix[0]) - 1
        while(low <= high):
            m = (low + high) // 2
            if(target > matrix[mid][m]):
                low = m + 1
            
            elif(target < matrix[mid][m]):
                high = m - 1
                
            else: return(True)
        
        return(False)
        
         
            
        
        
        
        """
        #Time Complexity (m + logn)
        for r in range(len(matrix)):
            if(target <= matrix[r][-1]):
                low = 0
                high = len(matrix[r])-1
                # mid = (high - low) // 2
                while(low <= high):
                    mid = (high + low) //2
                    if(matrix[r][mid] == target):
                        return(True)
                    
                    elif(matrix[r][mid] < target):
                        high = mid + 1
                    
                    else:
                        low = mid - 1
                break
        return(False)
        """     
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
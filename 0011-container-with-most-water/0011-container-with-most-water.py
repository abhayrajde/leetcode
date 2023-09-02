class Solution(object):
    def maxArea(self, height):
        # Two-Pointer - T.C: O(N)
        result = 0
        i = 0
        j = len(height)-1
        while(i<j):
            current_area = (j-i) * min(height[i],height[j])
            result = max(current_area,result)\
            
            if(height[i]<=height[j]):
                i+=1
            else:
                j-=1
        return(result)
        
        # #Brute-Force - Time Complexity: O(N^2)
        # result = 0
        # for i in range(len(height)-1):
        #     for j in range(i+1, len(height)):
        #         current_area = (j-i)*min(height[i],height[j])
        #         result = max(current_area,result)
        # return result
        """
        :type height: List[int]
        :rtype: int
        """
        
class Solution(object):
    def maxArea(self, height):
        i = 0
        j = len(height)-1
        area = []
        count = len(height) - 1
        while(i != j):
            area.append(min(height[i],height[j])*count)
            if(height[i]<height[j]):
                i+=1
            else:
                j-=1
            count-=1
        return(max(area))
        
        """
        :type height: List[int]
        :rtype: int
        """
        
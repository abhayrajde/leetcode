class Solution(object):
    def maxArea(self, height):
        start = 0
        end = len(height)-1
        max1 = 0
        while(start<end):
            temp = (end-start) * min(height[start],height[end])
            if(temp>max1):
                max1 = temp
            if(height[start]>=height[end]):
                end-=1
            else:
                start+=1
        return(max1)
        # i = 0
        # j = len(height)-1
        # area = []
        # count = len(height) - 1
        # while(i != j):
        #     area.append(min(height[i],height[j])*count)
        #     if(height[i]<height[j]):
        #         i+=1
        #     else:
        #         j-=1
        #     count-=1
        # return(max(area))
        
        """
        :type height: List[int]
        :rtype: int
        """
        
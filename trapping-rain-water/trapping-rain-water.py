class Solution(object):
    def trap(self, height):
        maxleft = []
        maxl = height[0]
        maxleft.append(maxl)
        for i in range(1,len(height)):
            if(height[i]>maxl):
                maxl = height[i]
                maxleft.append(maxl)
            else:
                maxleft.append(maxl)
        
        maxright = []
        maxr = height[-1]
        maxright.append(maxr)
        for i in range(len(height)-2,-1,-1):
            if(height[i]>maxr):
                maxr = height[i]
                maxright.append(maxr)
            else:
                maxright.append(maxr)
        maxright.reverse()
        
        minlr = []
        for i in range(len(height)):
            minlr.append(min(maxright[i],maxleft[i]))
        
        count = 0
        for i in range(len(height)):
            temp = minlr[i] - height[i]
            if(temp > 0):
                count += temp
        
        return(count)
            
            # start = height[i]
            
        """
        :type height: List[int]
        :rtype: int
        """
        
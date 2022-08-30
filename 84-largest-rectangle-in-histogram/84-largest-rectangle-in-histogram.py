class Solution(object):
    def largestRectangleArea(self, heights):
        maxarea = 0
        stack = [] # pair : (index,height)
        
        for i,h in enumerate(heights):
            start = i
            while(stack and stack[-1][1] > h):
                index,height = stack.pop()
                maxarea = max(maxarea,height * (i-index))
                start = index
                # stack.append()
            stack.append((start,h))
            
        for i,h in stack:
            maxarea = max(maxarea, h * (len(heights)-i))
        
        return maxarea
        """
        :type heights: List[int]
        :rtype: int
        """
        
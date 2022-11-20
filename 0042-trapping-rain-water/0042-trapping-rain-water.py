class Solution(object):
    def trap(self, height):
        l, r = 0, len(height)-1
        leftmax = height[l]
        rightmax = height[r]
        res = 0 
        
        while l < r:
            if leftmax < rightmax:
                l += 1
                leftmax = max(leftmax, height[l])
                res += leftmax - height[l]
            
            else:
                r -= 1
                rightmax = max(rightmax, height[r])
                res += rightmax -height[r]
        return res
        
        """
        :type height: List[int]
        :rtype: int
        """
        
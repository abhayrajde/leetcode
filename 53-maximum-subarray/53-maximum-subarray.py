class Solution(object):
    def maxSubArray(self, nums):
        max1 = nums[0]
        left, right = 0,0
        currsum = 0
        while(right<len(nums)):
            
            currsum+=nums[right]
            max1 = max(max1, currsum)
            
            if(currsum < 0):
                left = right+1
                currsum = 0
            
            right = right+1
        return(max1)
        """
        :type nums: List[int]
        :rtype: int
        """
        
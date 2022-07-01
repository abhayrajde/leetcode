class Solution(object):
    def maxSubArray(self, nums):
        max1 = nums[0]
        left, right = 0,0
        currsum = 0
        while(right<len(nums)):
            # print(nums[right])
            currsum+=nums[right]
            max1 = max(max1, currsum)
            # if(currsum > max1):
            #     max1 = currsum
            #     right+=1
                
            if(currsum < 0):
                left = right+1
                # right = right+1
                currsum = 0
            right = right+1
            # else:
                # right+=1
        return(max1)
        """
        :type nums: List[int]
        :rtype: int
        """
        
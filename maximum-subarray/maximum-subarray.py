class Solution(object):
    def maxSubArray(self, nums):
        
#         if(len(nums)==1):
#             op = nums[0]
#             return(op)
#         else: 
            
        
        max1 = nums[0]
        sum1 = 0
        
        for i in nums:
            sum1+=i
            if(sum1>max1):
                max1 = sum1
            if(sum1 < 0):
                sum1 = 0
            # else:
            #     if
        return (max1)
        """
        :type nums: List[int]
        :rtype: int
        """
        
class Solution(object):
    def rob(self, nums):
        
        # if the number of houses is 1 or 2 or 3 then may the richest house be robbed
        if(len(nums)==1 or len(nums)==2 or len(nums)==3):
            return(max(nums))
        
        #logic for more then 3 houses
        else:
            dp1 = [0]*len(nums)
            dp2 = [0]*len(nums)
            dp1[0],dp2[0] = 0,0
            dp1[1],dp2[1] = nums[0],nums[1]
            for i in range(2,len(dp1)):
                dp1[i] = max(dp1[i-1],dp1[i-2]+nums[i-1])
                
            for i in range(2,len(dp2)):
                dp2[i] = max(dp2[i-1], dp2[i-2]+nums[i])
            
            return(max(dp1[len(nums)-1],dp2[len(nums)-1]))
            
        """
        :type nums: List[int]
        :rtype: int
        """
        
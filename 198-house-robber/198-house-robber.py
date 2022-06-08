class Solution(object):
    def rob(self, nums):
        dp = [0]*(len(nums)+1)
        dp[0] = 0
        dp[1] = nums[0]
        for i in range(1,len(nums)):
            dp[i+1] = max(nums[i]+dp[i-1],dp[i])
        return(dp[len(nums)])
            
        """
        :type nums: List[int]
        :rtype: int
        """
        
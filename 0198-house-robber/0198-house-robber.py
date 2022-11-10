class Solution(object):
    def rob(self, nums):
        
        dp = [-1]*len(nums)
        
        
        def func(ind):
            if ind >= len(nums):
                return 0
            
            if dp[ind] != -1:
                return dp[ind]
            
            pick = nums[ind] + func(ind+2)
            
            not_pick = 0 + func(ind + 1)
            
            dp[ind] = max(pick, not_pick)
            
            return dp[ind]
        res = func(0)
        return res
            
        """
        :type nums: List[int]
        :rtype: int
        """
        
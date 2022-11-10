class Solution(object):
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]
        # dp = [-1] * len(nums)
        
        def func(house_list, dp, ind):
            if ind >= len(house_list):
                return 0
            
            if dp[ind] != -1:
                return dp[ind]
            
            pick = house_list[ind] + func(house_list, dp, ind + 2)
            not_pick = 0 + func(house_list,dp, ind + 1)
            
            dp[ind] = max(pick, not_pick)
            return dp[ind]
        
        keep_first = nums[:-1]
        # print(keep_first)
        keep_last = nums[1:]
        # print(keep_last)
        return max(func(keep_first,[-1]*len(keep_first),0),func(keep_last,[-1]*len(keep_last),0))
        
        """
        :type nums: List[int]
        :rtype: int
        """
        
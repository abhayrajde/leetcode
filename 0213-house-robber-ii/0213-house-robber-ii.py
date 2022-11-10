class Solution(object):
#     def rob(self, nums):
#         if len(nums) == 1:
#             return nums[0]
        
#         def dp_tab(nums):
#             dp = [0]*len(nums)

#             for i in range(len(nums)):
#                 pick = nums[i]

#                 if i>1:
#                     pick += dp[i-2]
#                 not_pick = 0
#                 if i > 0:
#                     not_pick += dp[i-1]

#                 dp[i] = max(pick,not_pick)

#             return(dp[-1])
#         keep_first = dp_tab(nums[:-1])
#         keep_last = dp_tab(nums[1:])
#         return max(keep_first,keep_last)
    
    #Memoization Technique
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]
        
        def dp_mem(nums):
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
        
        keep_first = dp_mem(nums[:-1])
        keep_last = dp_mem(nums[1:])
        return max(keep_first,keep_last)
    
    
#     #Memoization Technique
#     def rob(self, nums):
#         if len(nums) == 1:
#             return nums[0]
#         # dp = [-1] * len(nums)
        
#         def func(house_list, dp, ind):
#             if ind >= len(house_list):
#                 return 0
            
#             if dp[ind] != -1:
#                 return dp[ind]
            
#             pick = house_list[ind] + func(house_list, dp, ind + 2)
#             not_pick = 0 + func(house_list,dp, ind + 1)
            
#             dp[ind] = max(pick, not_pick)
#             return dp[ind]
        
#         keep_first = nums[:-1]
#         # print(keep_first)
#         keep_last = nums[1:]
#         # print(keep_last)
#         return max(func(keep_first,[-1]*len(keep_first),0),func(keep_last,[-1]*len(keep_last),0))
        
        """
        :type nums: List[int]
        :rtype: int
        """
        
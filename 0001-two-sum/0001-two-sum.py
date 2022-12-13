class Solution(object):
    def twoSum(self, nums, target):
        
        #Time C - O(N)
        #Space C - O(N)
        hm = {}
        
        for i in range(len(nums)):
            if((target-nums[i]) in hm):
                return(i,hm[target-nums[i]])
            else:
                hm[nums[i]] = i
        
        # we have to return the index, so sorting not allowed.
        
#         nums = sorted(nums)
        
#         l = 0
#         r = len(nums) - 1
#         while l < r:
#             if nums[l] + nums[r] == target:
#                 return([l,r])
#             if nums[l] + nums[r] < target:
#                 l += 1
#             else:
#                 r -= 1
        
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
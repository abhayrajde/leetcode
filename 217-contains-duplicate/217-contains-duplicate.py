class Solution(object):
    def containsDuplicate(self, nums):
        hm = {}
        for i in range(len(nums)):
            if(nums[i] not in hm):
                hm[nums[i]] = 1
            else:
                return(True)
            
        return(False)
        
        # Time and Space Complexity = O(N)
        # s1 = set(nums)
        # if(len(s1) == len(nums)):
        #     return(False)
        # else:
        #     return(True)
        """
        :type nums: List[int]
        :rtype: bool
        """
        
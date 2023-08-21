class Solution(object):
    def containsDuplicate(self, nums):
        hm = {}
        for i in range(len(nums)):
            if(nums[i] not in hm):
                hm[nums[i]] = 1
            else:
                return(True)
            
        return(False)
    
                
        """
        :type nums: List[int]
        :rtype: bool
        """
        
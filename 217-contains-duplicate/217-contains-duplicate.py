class Solution(object):
    def containsDuplicate(self, nums):
        s1 = set(nums)
        if(len(s1) == len(nums)):
            return(False)
        else:
            return(True)
        """
        :type nums: List[int]
        :rtype: bool
        """
        
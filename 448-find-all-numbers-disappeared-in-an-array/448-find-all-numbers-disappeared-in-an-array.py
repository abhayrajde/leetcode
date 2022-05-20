class Solution(object):
    def findDisappearedNumbers(self, nums):
        l = len(nums)
        set1 = set()
        for i in range(l):
            set1.add(i+1)
        
        for i in range(len(nums)):
            if(nums[i] in set1):
                set1.remove(nums[i])
        return(set1)
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
class Solution(object):
    def findDuplicate(self, nums):
        set1 = set()
        for i in nums:
            if(i not in set1):
                set1.add(i)
            else:
                return (i)
        """
        :type nums: List[int]
        :rtype: int
        """
        
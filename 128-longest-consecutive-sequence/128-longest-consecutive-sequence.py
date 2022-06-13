class Solution(object):
    def longestConsecutive(self, nums):
        set1 = set(nums)
        nums = list(set1)
        max_count = 0
        for i in nums:
            if(i-1 not in set1):
                count = 1
                while(i+1 in set1):
                    count += 1
                    i = i+1
                if(count > max_count):
                    max_count = count
        return(max_count)
            
        
        """
        :type nums: List[int]
        :rtype: int
        """
        
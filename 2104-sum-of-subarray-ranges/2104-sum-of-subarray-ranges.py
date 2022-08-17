class Solution(object):
    def subArrayRanges(self, nums):
        tot = 0
        for i in range(len(nums)-1):
            curr_min = nums[i]
            curr_max = nums[i]
            for j in range(i+1,len(nums)):
                curr_min = min(curr_min, nums[j])
                curr_max = max(curr_max, nums[j])
                tot += (curr_max - curr_min)
        return tot
        
        
        """
        :type nums: List[int]
        :rtype: int
        """
        
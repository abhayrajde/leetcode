class Solution(object):
    def subsetsWithDup(self, nums):
        res = []
        nums.sort()
        self.dfs(nums, [], res)
        return(res)
        
    def dfs(self, nums, curr, res):
        res.append(curr)
        for i in range(len(nums)):
            if(i>0 and nums[i] == nums[i-1]):
                continue
            self.dfs(nums[i+1:], curr+[nums[i]], res)
        
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
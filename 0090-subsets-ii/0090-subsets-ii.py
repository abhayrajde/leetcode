class Solution(object):
    def subsetsWithDup(self, nums):
        # Base Condition
        if not nums:
            return []
        
        nums= sorted(nums)
        res = []
        def dfs(i, curr):
            if i >= len(nums):
                res.append(curr[:])
                return
            
            pick = dfs(i+1, curr+[nums[i]])
            while(i < len(nums) - 1 and nums[i] == nums[i + 1]):
                i = i+1
            not_pick = dfs(i+1, curr)
        dfs(0,[])
        return res
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
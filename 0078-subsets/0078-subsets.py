# Pick - Not Pick Logic
# create one dfs/recursion function which takes i. current position ii. current subset
    # if the current position is greater than len(nums):
        # append current subset to the result
        #return
    #recursively call PICK
    # recursively call NOT PICK
    
class Solution(object):
    def subsets(self, nums):
        # Base Condition
        if not nums:
            return []
        
        res = []
        curr = []
        def dfs(i,curr):
            if i >= len(nums):
                res.append(curr[:])
                return
            
            pick = dfs(i+1,curr + [nums[i]])
            not_pick = dfs(i+1,curr)
        dfs(0,[])
        return res
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
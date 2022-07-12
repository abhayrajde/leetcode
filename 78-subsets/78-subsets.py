class Solution(object):
    def subsets(self, nums):
        res = []
        
        curr = []
        def dfs(i):
            if(i>=len(nums)):
                res.append(copy.copy(curr))
                return
            
            curr.append(nums[i])
            dfs(i+1)
            
            curr.pop()
            dfs(i+1)
        
        dfs(0)
        return(res)
            
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
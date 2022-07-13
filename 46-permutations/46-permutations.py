class Solution(object):
    def permute(self, nums):
        res = []
        self.dfs(nums, [], res)
        return(res)
        
    def dfs(self, dec_space, curr, res):
        if(not dec_space):
            res.append(curr)
            return
        
        for i in range(len(dec_space)):
            self.dfs(dec_space[:i]+dec_space[i+1:], curr+[dec_space[i]], res)
            
        
#         res = []
        
#         cur = []
#         def dfs(i):
#             if(i == len(nums)-1):
#                 res.append(copy.copy(cur))
#                 return
            
#             # if(i < len(nums)-1):
#             cur.append(nums[i])
#             dfs(i+1)
#             cur.pop()
        
            
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
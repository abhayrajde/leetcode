class Solution(object):
    def combinationSum2(self, candidates, target):
        res = []
        self.target = target
        candidates.sort()
        self.dfs(candidates, [], res)
        return(res)
        
    def dfs(self, candidates, curr, res):
        for i in range(len(candidates)):
            
            if(i > 0 and candidates[i] == candidates[i-1]):
                continue
            
            if(sum(curr)+candidates[i] == self.target):
                curr.append(candidates[i])
                res.append(curr)
                return
            
            if(sum(curr) + candidates[i] < self.target):
                self.dfs(candidates[i+1:], curr+[candidates[i]], res)
            
            else:
                return
        
        
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
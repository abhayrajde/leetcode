class Solution(object):
    def combinationSum(self, candidates, target):
        res = []
        def dfs(i,cur,total):
            if(total == target):
                res.append(copy.deepcopy(cur))
                return
            
            if(i>=len(candidates) or total>target):
                return
            cur.append(candidates[i])
            dfs(i,cur,total+candidates[i])
            cur.pop()
            dfs(i+1, cur, total)
        dfs(0,[],0)
        return(res)
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
class Solution(object):
    def combinationSum(self, candidates, target):
        res = []
        def dfs(i,cur,total):
            if(total == target):
                temp = copy.deepcopy(cur)
                res.append(temp)
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
        
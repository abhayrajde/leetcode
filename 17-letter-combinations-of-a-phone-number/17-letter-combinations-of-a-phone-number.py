class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
            return []
        mapping = {'2':"abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno", '7':"pqrs", '8':"tuv", '9':"wxyz"}
        res = []
        self.dfs(mapping,digits,"", res)
        return(res)
        
    def dfs(self, mapping, digits, curr, res):
        if(not digits):
            res.append(curr)
            return
        
        for c in mapping[digits[0]]:
            self.dfs(mapping, digits[1:], curr+c, res)
            
        
        """
        :type digits: str
        :rtype: List[str]
        """
        
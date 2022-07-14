class Solution(object):
    def partition(self, s):
        res = []
        self.dfs(s, [], res)
        return(res)
        
        
    def ispalindrome(self, s):
        return(s == s[::-1])

    def dfs(self, s, curr, res):
        if(not s):
            res.append(curr)
            return

        for i in range(len(s)):
            if(self.ispalindrome(s[:i+1])):
                self.dfs(s[i+1:], curr+[s[:i+1]], res)

                
        
        
        
        
        
        
        
        
        
        
        
        
        
        """
        res = []
        self.dfs(s, [], res)
        return res

    def dfs(self, s, path, res):
        if not s:
            res.append(path)
            return
        for i in range(1, len(s)+1):
            if self.isPal(s[:i]):
                self.dfs(s[i:], path+[s[:i]], res)

    def isPal(self, s):
        return s == s[::-1]
        """
        """
        :type s: str
        :rtype: List[List[str]]
        """
        
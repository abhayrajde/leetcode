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
        :type s: str
        :rtype: List[List[str]]
        """
        
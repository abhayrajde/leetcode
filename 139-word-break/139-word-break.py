class Solution(object):
    def wordBreak(self, s, wordDict):
        dp = [False]*(len(s)+1)
        dp[-1] = True
        sublen = len(s)
        for i in range(len(s)-1,-1,-1):
            for j in wordDict:
                if(i+len(j) <= len(s) and s[i:i+len(j)] == j):
                    dp[i] = dp[i+len(j)]
                if(dp[i] == True):
                    break
        return(dp[0])
                
                
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        
class Solution(object):
    def wordBreak(self, s, wordDict):
        
        # We will be using memoization technique in dp
        dp = {}
        
        def dfs(string):
            
            #if the string is available in dp dic which might have been encountered before than return that
            if string in dp:
                return dp[string]
            
            #if the string is empty
            if not string:
                return [""]
            
            local_res = []
            
            for word in wordDict:
                if string.startswith(word):
                    sub_words = dfs(string[len(word):])
                    
                    for sub_word in sub_words:
                        local_res.append(word + (" " if sub_word else "") + sub_word)
                        
            dp[string] = local_res
            
            return local_res
        return dfs(s)
            
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        
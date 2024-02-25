class Solution(object):
    def mergeAlternately(self, word1, word2):
        word1Len = len(word1)
        word2Len = len(word2)
        maxLen = max(word1Len, word2Len)
        outputString = ""
        for i in range (maxLen):
            if(i < word1Len):
                outputString += word1[i]
            if(i < word2Len):
                outputString += word2[i]
        return outputString
            
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        
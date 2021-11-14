class Solution(object):
    def longestCommonPrefix(self, strs):
        op = ""
        minlen = 1000
        for i in strs:
            if(len(i) < minlen):
                minlen = len(i)
        
        for i in range(minlen):
            common = strs[0][i]
            count = 0
            for j in range(len(strs)):
                if(strs[j][i] == common):
                    count += 1
                    
            if(count == len(strs)):
                op+=strs[0][i]
            else:
                break        

        return (op)    
        """
        :type strs: List[str]
        :rtype: str
        """
        
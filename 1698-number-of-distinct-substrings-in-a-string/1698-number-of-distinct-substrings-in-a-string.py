class Solution(object):
    def countDistinct(self, s):
        s_len = len(s)
        substrs = set()
        
        for i in range(len(s)):
            substr = ""
            substr += s[i]
            if substr not in substrs:
                substrs.add(substr)
            for j in range(i+1,len(s)):
                substr += s[j]
                if substr not in substrs:
                    substrs.add(substr)
        return len(substrs)
                
        """
        :type s: str
        :rtype: int
        """
        
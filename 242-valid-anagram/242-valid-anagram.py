class Solution(object):
    def isAnagram(self, s, t):
        s = sorted(s)
        t = sorted(t)
        if(s == t):
            return(True)
        else:
            return(False)
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
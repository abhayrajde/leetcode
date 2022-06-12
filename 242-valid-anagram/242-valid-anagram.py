class Solution(object):
    def isAnagram(self, s, t):
        #Using HashMap Logic
        
        if(len(s)!=len(t)):
            return(False)
        
        hms = {}
        hmt = {}
        for i in range(len(s)):
            if(s[i] in hms):
                hms[s[i]]+=1
            else:
                hms[s[i]] = 1
        
        for i in range(len(t)):
            if(t[i] in hmt):
                hmt[t[i]]+=1
            else:
                hmt[t[i]] = 1
        
        for i in range(len(s)):
            if((s[i] not in hmt) or (hms[s[i]] != hmt[s[i]])):
                return(False)
        return(True)
        
        
        
        #Using normal Sorting Technique - Time Complexity = 2nlogn +2n | Space = O(1)
        # s = sorted(s)
        # t = sorted(t)
        # if(s == t):
        #     return(True)
        # else:
        #     return(False)
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
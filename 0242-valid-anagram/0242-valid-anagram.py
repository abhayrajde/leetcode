class Solution(object):
    def isAnagram(self, s, t):
        
        if(len(s) != len(t)):
            return False
        
        hms = {}
        hmt = {}
        
        #elements count for string s
        for i in range(len(s)):
            if(s[i] not in hms):
                hms[s[i]] = 1
            else:
                hms[s[i]] += 1
        
        #elements count for string t
        for i in range(len(t)):
            if(t[i] not in hmt):
                hmt[t[i]] = 1
            else:
                hmt[t[i]] += 1
        
        #compare both the hashmap dictionary
        # if(len(t)>len(s)):
        #     s,t = t,s
        #     hms,hmt = hmt,hms
            
        for i in range(len(s)):
            if((s[i] not in hmt) or (hms[s[i]] != hmt[s[i]])):
                return False
        return True
    
        
        
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
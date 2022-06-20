class Solution(object):
    def minWindow(self, s, t):
        if t == "": return ""
        
        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        
        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            
            if c in countT and window[c] == countT[c]:
                have += 1
        
            while have == need:
                # update our result
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = (r - l + 1)
                # pop from the left of our window
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r+1] if resLen != float("infinity") else ""
        
        """
        if t == "": return ""
        
        have = {}
        need = {}
        for i in range(len(t)):
            need[t[i]] = 1+need.get(t[i],0)
        
        h,n = 0, len(need)
        res,reslen = [-1,-1], float("infinity")
        l = 0
        for r in range(len(s)):
            curr = s[r]
            have[curr] = 1 + have.get(curr,0)
            
            if(curr in need and have[curr] == need[curr]):
                h+=1
            
            while(h == n):
                if((r-l+1)<reslen): 
                    res = [l,r]
                    reslen = (r-1+1)
                have[s[l]] -= 1
                if(s[l] in need and have[s[l]]<need[s[l]]):
                    h-=1
                l+=1
        l,r = res
        return(s[l:r+1] if reslen != float("infinity") else "")
        """                
                
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
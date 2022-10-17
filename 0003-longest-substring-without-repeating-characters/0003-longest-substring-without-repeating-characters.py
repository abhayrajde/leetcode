class Solution(object):
    def lengthOfLongestSubstring(self, s):
        hm = {}
        op = 0
        l,r = 0,0
        while(r<len(s)):
            if(s[r] not in hm):
                hm[s[r]] = r
            else:
                l = max(l,hm[s[r]]+1)
                hm[s[r]] = r
            op = max(op,r-l+1)
            r+=1
        return(op)
        """
        :type s: str
        :rtype: int
        """
        
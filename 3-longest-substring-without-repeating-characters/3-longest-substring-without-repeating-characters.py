class Solution(object):
    def lengthOfLongestSubstring(self, s):
        # s = "abcabcbb"
        # s = "pwwkew"
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
        map1 = {}
        op = 0
        # i = 0
        l = 0
        r = 0
        while (r < len(s)):
            if(s[r] not in map1):
                map1[s[r]] = r
                # r += 1

            else:
                l = max(l , map1[s[r]]+1)
                map1[s[r]] = r
                # r += 1
            op = max(op,(r-l+1))
            r+=1
        return(op)
        """               
        """
        :type s: str
        :rtype: int
        """
        
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        # s = "abcabcbb"
        # s = "pwwkew"
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
        list1 = [] 
        op = ""
        temp1 = ""
        for i in range(len(s)):
            if(s[i] not in list1):
                list1.append(s[i])
                temp1 += s[i]
                if(len(temp1)>len(op)):
                    op = temp1
            else:
                list1 = []       # we will overwrite list1 and make it blank
                list1.append(s[i])
                temp1 = s[i]
                if(len(temp1)>len(op)):
                    op = temp1
        return(len(op))
        """                
        """
        :type s: str
        :rtype: int
        """
        
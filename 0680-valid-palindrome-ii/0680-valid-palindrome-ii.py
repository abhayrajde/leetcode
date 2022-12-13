class Solution(object):
    def validPalindrome(self, s):
        l,r = 0, len(s) - 1
        
        while l < r:
            if s[l] != s[r]:
                skipl,skipr = s[l + 1:r + 1], s[l:r]
                return skipl == skipl[::-1] or skipr == skipr[::-1]
            l, r = l + 1, r - 1
        return True
        """
        :type s: str
        :rtype: bool
        """
        
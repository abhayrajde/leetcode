class Solution(object):
    def longestPalindrome(self, s):
        # if(len(s) == 1):
        #     return(s)
        # else:
        pal = ""
        pal_len = 0
        
        # In this loop i will be the center of palindrome
        for mid in range(len(s)):
            # if (mid == 0):
            #     pal = s[0]
            
            # else:    
            # for odd palindrome
            i = mid
            j = mid
            while(i>=0 and j<len(s) and s[i] == s[j]):
                if(j-i+1>pal_len):
                    pal = s[i:j+1]
                    pal_len = len(pal)
                i-=1
                j+=1


            # for even length palindrome
            i = mid
            j = mid+1
            while(i>=0 and j<len(s) and s[i] == s[j]):
                if(j-i+1>pal_len):
                    pal = s[i:j+1]
                    pal_len = len(pal)
                i-=1
                j+=1
        return(pal)

            
            
        """
        :type s: str
        :rtype: str
        """
        
class Solution(object):
    def countSubstrings(self, s):
        count = 0
        for mid in range(len(s)):
            
            #for odd length palindrome
            i,j = mid,mid
            while(i>=0 and j<len(s) and s[i] == s[j]):
                count+=1
                i-=1
                j+=1
            
            #for even length palindrome
            i,j = mid,mid+1
            while(i>=0 and j<len(s) and s[i] == s[j]):
                count+=1
                i-=1
                j+=1
        return(count)
        """
        :type s: str
        :rtype: int
        """
        
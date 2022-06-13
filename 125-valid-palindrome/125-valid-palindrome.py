class Solution(object):
    def isPalindrome(self, s):
        s = s.lower()
        str1 = ""
        for i in s:
            if(i.isalnum()):
                str1+=i
        i,j = 0,len(str1)-1
        while(i<j):
            if(str1[i]!=str1[j]):
                return(False)
            i+=1
            j-=1
        return(True)
        """
        :type s: str
        :rtype: bool
        """
        
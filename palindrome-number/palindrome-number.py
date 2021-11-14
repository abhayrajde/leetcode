class Solution(object):
    def isPalindrome(self, x):
        temp1 = str(x)
        temp2 = temp1[-1::-1]
        if(temp1 == temp2):
            return(True)
        else:
            return(False)
        """
        :type x: int
        :rtype: bool
        """
        
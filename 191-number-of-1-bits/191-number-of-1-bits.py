class Solution(object):
    def hammingWeight(self, n):
        res = 0
        while(n > 0):
            res += n%2
            n = n>>1
        return(res)
        """
        :type n: int
        :rtype: int
        """
        
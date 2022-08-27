class Solution(object):
    def numberOfWays(self, s):
        n = len(s)
        pre0 = [0]*n
        pre1 = [0]*n
        
        for i in range(n):
            if(s[i] == "0"):
                if(i == 0):
                    pre0[0] = 1
                else:
                    pre0[i] = pre0[i-1]+1
                    pre1[i] = pre1[i-1]
            else:
                if(i == 0):
                    pre1[0] = 1
                else:
                    pre1[i] = pre1[i-1]+1
                    pre0[i] = pre0[i-1]
        res = 0
        for i in range(1,n-1):
            if(s[i] == "0"):
                x = pre1[i-1]
                y = pre1[n-1] - pre1[i]
                res += (x*y)
            else:
                x = pre0[i-1]
                y = pre0[n-1] - pre0[i]
                res += (x*y)
        return res
                
        """
        :type s: str
        :rtype: int
        """
        
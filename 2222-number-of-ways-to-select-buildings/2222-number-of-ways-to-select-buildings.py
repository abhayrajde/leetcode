class Solution(object):
    def numberOfWays(self, s):
        pre0 = [0]*len(s)
        pre1 = [0]*len(s)
        n = len(s)
        
        for i in range(len(s)):
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
        for i in range(1,len(s)-1):
            if(s[i] == "0"):
                x = pre1[i-1]
                y = pre1[n-1] - pre1[i]
                res += (x*y)
            else:
                x = pre0[i-1]
                y = pre0[n-1] - pre0[i]
                res += (x*y)
                # res += (pre0[i-1]*pre0[n-1])
        return res
                
        """
        :type s: str
        :rtype: int
        """
        
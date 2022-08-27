class Solution(object):
    def numberOfWays(self, s):
        dp = {"0": 0, "1": 0, "01": 0, "10": 0, "010": 0, "101": 0}
        for i in range(len(s)):
            if s[i] == "0":
                dp["0"] += 1
                dp["10"] += dp["1"]
                dp["010"] += dp["01"]
            if s[i] == "1":
                dp["1"] += 1
                dp["01"] += dp["0"]
                dp["101"] += dp["10"]
                
        return dp["010"] + dp["101"]
        '''
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
        '''        
        """
        :type s: str
        :rtype: int
        """
        
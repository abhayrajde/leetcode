class Solution(object):
    def climbStairs(self, n):
        if(n == 1):
            return(1)
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2,n+1):
            dp[i] = dp[i-1]+dp[i-2]
        return(dp[n])
        # one = 1
        # two = 1
        # for i in range (n-1):
        #     temp = one
        #     one = one+two
        #     two = temp
        # return(one)
            
        """
        :type n: int
        :rtype: int
        """
        
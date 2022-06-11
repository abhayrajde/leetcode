class Solution(object):
    def coinChange(self, coins, amount):
        dp = [amount+1] *(amount+1)
        dp[amount] = 0
        for i in range(amount-1,-1,-1):
            for j in range(len(coins)):
                if(i + coins[j] <=amount):
                    dp[i] = min(dp[i],1+dp[i+coins[j]])
        if(dp[0]>amount):
            return(-1)
        else:
            return(dp[0])
                    
        # matrix=[[[0]*amount]*len(coins)]
        # for i in range(len(matrix)):
        #     for j in range(len(matrtix[0])):
        #         if(j>=coin[i]):
        #             matrix[i][j] = min(matrix[i-1][j],matrix[i][j-coin[i]])
        #         else:
        #             matrix[i][j] = matrix[i-1][j]
                    
            
                    
        
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
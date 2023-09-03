class Solution(object):
    def maxProfit(self, prices):
        total_profit = 0
        buy = prices[0]
        for i in range(1,len(prices)):
            profit = prices[i]-buy
            if (profit > 0):
                total_profit+=profit
                buy = prices[i]
            else:
                buy = prices[i]
        return total_profit
        """
        :type prices: List[int]
        :rtype: int
        """
        
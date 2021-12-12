class Solution(object):
    def maxProfit(self, prices):
        '''
        if(len(prices)<2):
            return(0)
        else:

            dict1 = {}
            dict2 = {}
            min1 = prices[0]
            min_index = 0
            for i in range(len(prices)):
                if(prices[i]<min1):
                    min1 = prices[i]
                    dict1[i] = min1
                    min_index = i
                else:
                    dict1[i] = min1
            print(min_index)
            print(dict1)
            max1 = prices[-1]
            max_index = len(prices)-1
            for j in range(len(prices)-1,min_index,-1):
                if(prices[j]>max1):
                    max1 = prices[j]
                    dict2[j] = max1
                    max_index = j
                else:
                    dict2[j] = max1
            print(max_index)
            print(dict2)
            op = prices[max_index]-prices[min_index]
            if(op>0):
                return(op)
            else:
                return(0)
        '''
        
        max_profit = 0
        buy = prices[0]
        for i in range(1,len(prices)):
            profit = prices[i]-buy
            
            if(profit>max_profit):
                max_profit = profit
            if(buy>prices[i]):
                buy = prices[i]
        return(max_profit)
        
        """
        :type prices: List[int]
        :rtype: int
        """
        
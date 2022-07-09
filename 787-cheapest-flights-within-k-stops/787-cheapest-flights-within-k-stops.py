# import Copy
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        prices = [float("inf")] * n
        prices[src] = 0
        for i in range(k+1):
            temp = copy.copy(prices)
            for s,d,p in flights:
                if(prices[s] == float("inf")):
                    continue
                if(prices[s] + p < temp[d]):
                    temp[d] = prices[s] + p
            prices = temp
        if(prices[dst] == float("inf")):
            return(-1)
        return(prices[dst])
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        
class Solution(object):
    def platesBetweenCandles(self, s, queries):
        n = len(s)
        prefix_sum = [0]*n
        candle_left = [-1]*n
        
        if(s[0] == "*"):
            prefix_sum[0] = 1
        if(s[0] == "|"):
            candle_left[0] = 0
            
        for i in range(1,n):
            if(s[i] == "*"):
                prefix_sum[i] = prefix_sum[i-1]+1
            else:
                prefix_sum[i] = prefix_sum[i-1]
            
            if(s[i] == "|"):
                candle_left[i] = i
            else:
                candle_left[i] = candle_left[i-1]
                
        candle_right = [n]*n
        if(s[n-1] == "|"):
            candle_right[n-1] = n-1
        
        for i in range (n-2,-1,-1):
            if(s[i] == "|"):
                candle_right[i] = i
            else:
                candle_right[i] = candle_right[i+1]
        
        res = [0]*len(queries)
        for i in range(len(queries)):
            start = candle_right[queries[i][0]]
            end = candle_left[queries[i][1]]
            if(start>=end):
                res[i] = 0
            else:
                res[i] = prefix_sum[end] - prefix_sum[start]
            
        return res
        
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        
class Solution(object):
    def minimumAbsDifference(self, arr):
        res = []
        
        arr.sort()
        
        minimum_diff = float("inf")
        for i in range(1,len(arr)):
            minimum_diff = min(minimum_diff,abs(arr[i]-arr[i-1]))
        
        for i in range(1,len(arr)):
            if(abs(arr[i] - arr[i-1]) == minimum_diff):
                res.append([arr[i-1],arr[i]])
        return(res)
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        
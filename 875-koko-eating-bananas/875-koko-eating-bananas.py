class Solution(object):
    def minEatingSpeed(self, piles, h):
        l = 1
        r = max(piles)
        res = r
        
        while(l <= r):
            k = (l + r)//2
            
            hours = 0
            for p in piles:
                hours += math.ceil((p-1)/ k)+1
            
            if(hours <= h):
                res = min(res, k)
                r = k - 1
            
            else:
                l = k + 1
        return(res)
        
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        
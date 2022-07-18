class Solution(object):
    def lastStoneWeight(self, stones):
        
        #Python doesnt have maxheap so using the concept of minheap
        for i in range(len(stones)):
            stones[i] = -1*stones[i]
            
        heapq.heapify(stones)
        
        while(len(stones) > 1):
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            if(y > x):
                x = abs(x)
                y = abs(y)
                heapq.heappush(stones,y - x)
        if(len(stones)==0):
            return(0)    
        return(-1*(stones[0]))
            
            
        """
        :type stones: List[int]
        :rtype: int
        """
        
class Solution(object):
    def kClosest(self, points, k):
        distheap = []
        for i,j in points:
            dist = sqrt(i**2 + j**2)
            distheap.append([dist,i,j])
        
        heapq.heapify(distheap)
        res = []
        while(k>0):
            dist,i,j = heapq.heappop(distheap)
            res.append([i,j])
            k-=1
        return(res)
            
        
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        
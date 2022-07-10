class Solution(object):
    def minCostConnectPoints(self, points):
        n = len(points)
        adj = {} # i : list of[cost,node]
        for i in range(n):
            adj[i] = []
        
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1,n):
                x2, y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                adj[i].append([dist,j])
                adj[j].append([dist,i])
        
        #Prim's
        res = 0
        visit = set()
        minh = [[0,0]] # [cost,point] --> so that we will start from the zero'th point in adj
        while(len(visit) < n):
            cost, i = heapq.heappop(minh)
            if i in visit:
                continue
            res += cost
            visit.add(i)
            for neicost,nei in adj[i]:
                heapq.heappush(minh,[neicost,nei])
        return(res)
            
            
        """
        :type points: List[List[int]]
        :rtype: int
        """
        
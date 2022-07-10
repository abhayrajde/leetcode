class Solution(object):
    def findRedundantConnection(self, edges):
        par = []
        for i in range(len(edges)+1):
            par.append(i)
        
        rank = [1] * (len(edges)+1)
        
        def find(n):
            p = par[n]
            while(p!=par[p]):
                p = par[p]
            return p
        
        def union(n1,n2):
            p1,p2 = find(n1), find(n2)
            
            if(p1 == p2):
                return(False)
            
            if(rank[p1] > rank[p2]):
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return(True)
        
        for n1,n2 in edges:
            if not union(n1,n2):
                return([n1,n2])
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        
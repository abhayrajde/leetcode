class Solution(object):
    def findItinerary(self, tickets):
        # Creating the blank adjecency disctionary
        adj = {}
        for src,dst in tickets:
            adj[src] = []
        
        tickets.sort()
        for src,dst in tickets:
            adj[src].append(dst)
        
        res = ["JFK"]
        def dfs(src):
            if(len(res) == len(tickets)+1):
                return(True)
            
            if(src not in adj):
                return(False)
            
            temp = list(adj[src])
            for i, nei in enumerate(temp):
                adj[src].pop(i)
                res.append(nei)
                if(dfs(nei)):
                    return(True)
                adj[src].insert(i,nei)
                res.pop()
            return(False)
          
        dfs("JFK")
        return(res)
        
        
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        
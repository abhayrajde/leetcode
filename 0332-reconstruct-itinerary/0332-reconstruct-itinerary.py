class Solution(object):
    def findItinerary(self, tickets):
        
        adj = {src:[] for src,dst in tickets}
        
        #sort first to get all the itenary in lexographical order
        #so that while adding the routes in dictionary it will be added itself in lexographical order.
        tickets.sort()
        
        #populate the adjescency dictionary
        for src, dst in tickets:
            adj[src].append(dst)
        
        res = ["JFK"]
        def dfs(src):
            #if we get all the options + 1(JFK by default) in result then direct return
            if len(res) == len(tickets)+1:
                return True
            
            if src not in adj:
                return False
            
            temp = list(adj[src])
            for i,v in enumerate(temp):
                res.append(v)
                adj[src].pop(i)
                if dfs(v):
                    return True
                adj[src].insert(i,v)
                res.pop()
            return False
        
        dfs("JFK")
        return res
            
        
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        
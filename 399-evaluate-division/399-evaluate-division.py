class Solution(object):
    def calcEquation(self, equations, values, queries):
        graph = collections.defaultdict(dict)
        
        #STEP 1 : CREATE GRAPH
        for (x,y),val in zip(equations,values):
            graph[x][y] = val
            graph[y][x] = 1.0/val
        
        
        #STEP 2 : THE DFS FUNCTION
        def dfs(x,y,visited):
            if(x not in graph or y not in graph):
                return -1.0
            
            if(y in graph[x]):
                return graph[x][y]
            
            for i in graph[x]:
                if i not in visited:
                    visited.add(i)
                    temp = dfs(i,y,visited)
                    if(temp == -1.0):
                        continue
                    else:
                        return graph[x][i] * temp
            return -1
        
        res = []
        for x,y in queries:
            res.append(dfs(x,y,set()))
        return res
        
        
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        
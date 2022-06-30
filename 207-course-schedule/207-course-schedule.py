class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        premap = {}
        
        for i in range(numCourses):
            premap[i] = []
        
        for crs, pre in prerequisites:
            premap[crs].append(pre)
        
        visited = set()
        def dfs(crs):
            if(crs in visited):
                return(False)
            
            if(premap[crs] == []):
                return(True)
            
            visited.add(crs)
            for pre in premap[crs]:
                if(not dfs(pre)):
                    return(False)
            visited.remove(crs)
            premap[crs] = []
            return(True)
        for crs in range(numCourses):
            if(not dfs(crs)): 
                return(False)
        return(True)
                
        
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
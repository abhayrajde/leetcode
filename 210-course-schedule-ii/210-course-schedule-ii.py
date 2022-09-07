class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        prereq = {c:[] for c in range(numCourses)}
        
        for crs,pre in prerequisites:
            prereq[crs].append(pre)
            
        output = []
        visited, cycle = set(), set()
        
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True
            
            cycle.add(crs)
            for pre in prereq[crs]:
                if(dfs(pre) == False):
                    return False
            cycle.remove(crs)
            visited.add(crs)
            output.append(crs)
            return True
        
        for crs in prereq:
            if(dfs(crs) == False):
                return []
        return output
            
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        
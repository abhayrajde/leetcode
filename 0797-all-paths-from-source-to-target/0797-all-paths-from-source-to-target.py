class Solution(object):
    def allPathsSourceTarget(self, graph):
        conn_map = defaultdict(list)
        
        start = 0
        end = len(graph)-1
        
        for source, target_list in enumerate(graph):
            for i in target_list:
                conn_map[source].append(i)
        
        res = []
        curr_path = []
        def dfs(curr, curr_path):
            
            if curr == end:
                curr_path.append(curr)
                res.append(curr_path[:])
                # curr_path.remove(curr)
                return
            
            # curr_path.append(curr)
            #TODO BUSINESS logic
            for next in conn_map[curr]:
                dfs(next,curr_path+[curr])
            # curr_path.remove(curr)
        dfs(0,curr_path)
        return res
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        
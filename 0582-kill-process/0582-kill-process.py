class Solution(object):
    def killProcess(self, pid, ppid, kill):
        
        graph = defaultdict(list)
        
        for child,parent in zip(pid,ppid):
            graph[parent].append(child)
            
        q = deque([kill])
        res = []
        while q:
            for i in range(len(q)):
                curr = q.popleft()
                res.append(curr)
                if curr in graph:
                    q.extend(graph[curr])
        return res
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        
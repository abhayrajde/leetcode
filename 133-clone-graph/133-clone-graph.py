"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        if(not node):
            return
        track = {}
        
        def dfs(node):
            if(node in track):
                return(track[node])
            
            copy = Node(node.val)
            track[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return(copy)
        return dfs(node)
        
        """
        :type node: Node
        :rtype: Node
        """
        
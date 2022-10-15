# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalTraversal(self, root):
        if not root: return
        v_dist = 0
        h_dist = 0
        values = defaultdict(list)
        res = []
        
        def verticalorder(node, h_dist, v_dist, values):
            if not node:
                return
            
            values[h_dist].append((v_dist,node.val))
            
            verticalorder(node.left, h_dist-1, v_dist+1, values)
            verticalorder(node.right, h_dist+1, v_dist+1, values)
        
        verticalorder(root,h_dist, v_dist, values)
        
        for x in sorted(values.keys()):
            column = []
            for i in sorted(values[x]):
                column.append(i[1])
            res.append(column)
        
        return res
            
            
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
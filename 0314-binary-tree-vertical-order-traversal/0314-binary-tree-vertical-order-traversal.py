# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalOrder(self, root):
        if not root: return
        
        h_dist = 0
        v_dist = 0
        values = defaultdict(list)
        res = []
        
        def dfs(node, h_dist, v_dist, values):
            # Base Condition
            if not node:
                return
            
            values[v_dist].append((h_dist,node.val))
            
            left = dfs(node.left, h_dist+1, v_dist-1, values)
            right = dfs(node.right, h_dist+1, v_dist+1, values)
            
        dfs(root, 0, 0, values)
        values = sorted(values.items(), key = lambda x:x[0])
        print(values)
        
        for key,value in values:
            temp1 = sorted(value, key = lambda x:x[0])
            temp2 = []
            for h_dist,val in temp1:
                temp2.append(val)
            res.append(temp2)
        return res
        
        
        
        
        
        
#         if not root: return
#         v_dist = 0
#         h_dist = 0
#         values = defaultdict(list)
#         res = []
        
#         def dfs(node, h_dist, v_dist, values):
#             if not node:
#                 return
            
#             values[h_dist].append((v_dist,node.val))
            
#             dfs(node.left, h_dist-1, v_dist+1, values)
#             dfs(node.right, h_dist+1, v_dist+1, values)
        
#         dfs(root,h_dist, v_dist, values)
        
#         for x in sorted(values.keys()):
#         # for x in values.keys():
#             column = []
#             for i in sorted(values[x]):
#             # for i in values[x]:
#                 column.append(i[1])
#             res.append(column)
        
#         return res
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
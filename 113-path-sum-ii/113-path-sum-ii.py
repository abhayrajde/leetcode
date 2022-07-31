# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        currsum = 0
        res = []
        def dfs(node, currsum,currpath):
            if(not node):
                return
            sum1 = currsum+node.val
            print(sum1)
            if(sum1 == targetSum and not node.right and not node.left):
                currpath+=[node.val]
                res.append(currpath)
            dfs(node.left,currsum+node.val,currpath+[node.val])
            dfs(node.right,currsum+node.val,currpath+[node.val])
        dfs(root,currsum,[])
        return res    
        
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        res = []
        node = root
        def dfs(node):
            if(not node):
                res.append("N")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(node)
        # return(",".join(res))
        str1 = ",".join(res)
        return(str1)
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        

    def deserialize(self, data):
        res = data.split(",")
        self.i = 0
        def dfs():
            if(res[self.i] == "N"):
                self.i+=1
                return (None)
            node = TreeNode(int(res[self.i]),None,None)
            self.i+=1
            node.left = dfs()
            node.right = dfs()
            return(node) 
        return(dfs())
        
        
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
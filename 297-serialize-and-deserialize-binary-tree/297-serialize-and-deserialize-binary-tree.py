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
        return(",".join(res))
        
        
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
    
    def deserialize(self, data):
        ip = data.split(",")
        self.i = 0
        def dfs():
            if(ip[self.i] == "N"):
                self.i+=1
                return(None)
            node = TreeNode(int(ip[self.i]),None,None)
            self.i+=1
            node.left = dfs()
            node.right = dfs()
            return(node)
        return dfs()
        
        
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
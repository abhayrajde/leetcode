class Node(object):
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.prev = self.next = None
        
class LRUCache(object):

    def __init__(self, capacity):
        self.cap = capacity
        self.cache = {}
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next = self.right.prev
        self.right.prev = self.left
        """
        :type capacity: int
        """
        
    def remove(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    #insert at the right
    def insert(self,node):
        node.prev = self.right.prev
        node.next = self.right
        self.right.prev.next = node
        self.right.prev = node
        
        
    def get(self, key):
        if(key in self.cache):
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return(self.cache[key].val) #why .val?
        return -1
        """
        :type key: int
        :rtype: int
        """
        

    def put(self, key, value):
        if(key in self.cache):
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])
        
        if(len(self.cache)>self.cap):
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        
        
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
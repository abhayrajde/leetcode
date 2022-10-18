class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache(object):

    def __init__(self, capacity):
        self.cap = capacity
        self.cache = {} # map key to node
        
        #Left - will help to find least recently used Node
        #Right - will help to find the most recent
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left
        
        """
        :type capacity: int
        """
    
    # remove node from the list
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev
        
    # insert node in the list at the right
    def insert(self,node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev
        
    
    def get(self, key):
        if key in self.cache:
            #TODO: update the most recent 
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        
        return -1
        
        """
        :type key: int
        :rtype: int
        """
        

    def put(self, key, value):
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])
        
        if len(self.cache) > self.cap:
            # remove from the list and delete thr LRU from the hashmap
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
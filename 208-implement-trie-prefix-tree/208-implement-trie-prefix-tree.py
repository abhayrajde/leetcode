class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.endofword = False
        
class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        
        for i in word:
            if(i not in curr.children):
                curr.children[i] = TrieNode()
            curr = curr.children[i]
        curr.endofword = True
        
        """
        :type word: str
        :rtype: None
        """
        

    def search(self, word):
        curr = self.root
        
        for i in word:
            if(i not in curr.children):
                return(False)
            curr = curr.children[i]
        return(curr.endofword)
    
        
        """
        :type word: str
        :rtype: bool
        """
        

    def startsWith(self, prefix):
        curr = self.root
        
        for i in prefix:
            if(i not in curr.children):
                return(False)
            curr = curr.children[i]
        return(True)
        
        """
        :type prefix: str
        :rtype: bool
        """
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
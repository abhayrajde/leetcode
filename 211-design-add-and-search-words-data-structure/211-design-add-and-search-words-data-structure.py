class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.endofword = False
        
class WordDictionary(object):

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
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
        def dfs(j,root):
            curr = root

            for i in range(j,len(word)):
                c = word[i]

                if(c == "."):
                    for child in curr.children.values():
                        if(dfs(i+1,child)):
                            return(True)
                    return(False)

                else:
                    if(c not in curr.children):
                        return(False)
                    curr = curr.children[c]
            return(curr.endofword)
        return(dfs(0,self.root))
        """
        :type word: str
        :rtype: bool
        """
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
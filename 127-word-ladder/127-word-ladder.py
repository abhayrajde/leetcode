class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        
        nei = {}
        wordList.append(beginWord)
        
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                if(pattern not in nei):
                    nei[pattern] = []
                nei[pattern].append(word)
                
                
        visited = set([beginWord])
        q = deque([beginWord])
        res = 1
        while(q):
            for i in range(len(q)):
                word = q.popleft()
                if(word == endWord):
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for neiword in nei[pattern]:
                        if(neiword not in visited):
                            visited.add(neiword)
                            q.append(neiword)
            res+=1
        return 0
                    
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        
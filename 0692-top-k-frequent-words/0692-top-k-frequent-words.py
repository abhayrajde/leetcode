class Solution(object):
    def topKFrequent(self, words, k):
        count = {}
        freq = [[] for i in range(len(words)+1)]
        
        for word in words:
            count[word] = 1 + count.get(word,0)
        
        for word,c in count.items():
            freq[c].append(word)
        
        res = []
        for i in range(len(freq)-1,0,-1):
            for word in sorted(freq[i]):
                res.append(word)
                if len(res) == k:
                    return res
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        
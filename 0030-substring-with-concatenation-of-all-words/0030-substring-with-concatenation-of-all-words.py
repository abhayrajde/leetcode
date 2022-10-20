class Solution(object):
    def findSubstring(self, s, words):
        w_len = len(words[0])
        tot_words = len(words)
        res = []
        present = Counter(words)
        
        i = 0
        
        
        def concat_check(inp_str):
            chunks = {}
            for i in range(0,w_len*tot_words,w_len):
                curr = inp_str[i:i+w_len]
                if curr not in chunks:
                    chunks[curr] = 0
                chunks[curr]+=1
                
            for i in chunks:
                if i not in present or present[i] != chunks[i]:
                    return False
            
            return True
        
        i = 0
        while i < len(s):
            if i+(w_len*tot_words)-1 < len(s):
                if concat_check(s[i:i+(w_len*tot_words)]):
                    res.append(i)
                    
            i += 1
        
        return res
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        
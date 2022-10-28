class Solution(object):
    def minSteps(self, s, t):
        # dict_s = defaultdict(int)
        dict_t = defaultdict(int)
        
        # for i in s:
        #     dict_s[i] += 1
            
        for i in t:
            dict_t[i] += 1
            
        count = 0
        
        for i in s:
            if i not in dict_t or dict_t[i] == 0:
                count+=1
            else:
                dict_t[i] -=1
        return count
            
        
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        
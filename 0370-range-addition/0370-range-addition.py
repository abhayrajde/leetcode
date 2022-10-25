class Solution(object):
    def getModifiedArray(self, length, updates):
        
        start_dic = defaultdict(int)
        end_dic = defaultdict(int)
        
        for s,e,inc in updates:
            start_dic[s] += inc
            end_dic[e] += inc
        
        res = [0]*length
        counter = 0
        
        for i in range(length):
            if i in start_dic:
                counter += start_dic[i]
            
            res[i] += counter
            
            if i in end_dic:
                counter -= end_dic[i]
        
        return res
                
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        
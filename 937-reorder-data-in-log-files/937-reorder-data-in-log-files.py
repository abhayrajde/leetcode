class Solution(object):
    def reorderLogFiles(self, logs):
        res1 = []
        res2 = []
        
        for i in range(len(logs)):
            if(logs[i].split()[1]).isdigit():
                res2.append(logs[i])
            else:
                res1.append(logs[i].split())
        res1.sort(key = lambda x:x[0])
        res1.sort(key = lambda x:x[1:])
        
        for i in range(len(res1)): 
            res1[i] =(" ".join(res1[i]))
        res1.extend(res2)
        return res1
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        
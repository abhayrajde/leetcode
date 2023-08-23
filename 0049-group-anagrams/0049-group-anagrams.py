class Solution(object):
    def groupAnagrams(self, strs):
        
        hm = {}
        for i in range(len(strs)):
            temp = str(sorted(strs[i]))
            if(temp in hm):
                hm[temp].append(strs[i])
            else:
                hm[temp] = [strs[i]]
        op = []
        for i in (hm.values()):
            op.append(i)
        return(op)
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
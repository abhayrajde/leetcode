class Solution(object):
    def groupAnagrams(self, strs):
        # check if we can use trie for this question!!!!!!
        
        hm = {}
        for i in range(len(strs)):
            temp = sorted(strs[i])
            # temp1 = temp[0:-1]
            temp1 = ""
            for j in range(len(temp)):
                temp1+=temp[j]
            if(temp1 in hm):
                hm[temp1].append(strs[i])
            else:
                hm[temp1] = [strs[i]]
        op = []
        for i in (hm.values()):
            op.append(i)
        return(op)
            
            
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
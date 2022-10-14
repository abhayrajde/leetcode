class Solution(object):
    def twoCitySchedCost(self, costs):
        #Using Greedy Method
        diffs = []
        for ca,cb in costs:
            diffs.append([cb-ca,ca,cb])
        diffs.sort()
        
        res = 0
        for i in range(len(diffs)):
            if i < len(diffs)//2:
                res+=diffs[i][2]
            else:
                res+=diffs[i][1]
        return res
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        
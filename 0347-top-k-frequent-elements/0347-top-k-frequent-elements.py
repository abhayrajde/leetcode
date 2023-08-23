class Solution(object):
    def topKFrequent(self, nums, k):
        hm = defaultdict(int)
        
        for i in nums:
            hm[i]+=1
        
        hm = sorted(hm.items(), key = lambda x:x[1], reverse = True)
        result = []
        for i in range(k):
            result.append(hm[i][0])
        return result
            
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
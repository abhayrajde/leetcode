class Solution(object):
    def topKFrequent(self, nums, k):
        hm = {}
        for i in range(len(nums)):
            if(nums[i] in hm):
                hm[nums[i]] += 1
            else:
                hm[nums[i]] = 1
        hm = sorted(hm.items(), key = lambda x:x[1], reverse = True)
        op = []
        for i in range(k):
            op.append(hm[i][0])
        return(op)
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
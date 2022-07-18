class Solution(object):
    def findKthLargest(self, nums, k):
        for i in range(len(nums)):
            nums[i] = -1*(nums[i])
        
        heapq.heapify(nums)
        
        while(k>0):
            res = heapq.heappop(nums)
            k-=1
        return(-(res))
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
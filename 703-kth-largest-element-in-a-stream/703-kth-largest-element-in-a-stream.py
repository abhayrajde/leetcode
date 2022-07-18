class KthLargest(object):

    def __init__(self, k, nums):
        self.minheap = nums
        self.k = k 
        heapq.heapify(self.minheap)
        while(len(self.minheap) > self.k):
            heapq.heappop(self.minheap)
        """
        :type k: int
        :type nums: List[int]
        """
        

    def add(self, val):
        heapq.heappush(self.minheap, val)
        if(len(self.minheap) > self.k):
            heapq.heappop(self.minheap)
        return(self.minheap[0])
        """
        :type val: int
        :rtype: int
        """
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
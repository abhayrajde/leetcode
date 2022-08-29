class NumArray(object):

    def __init__(self, nums):
        self.nums = nums
        self.sumnums = [0]*len(nums)
        self.sumnums[0] = nums[0]
        for i in range(1,len(nums)):
            self.sumnums[i] = self.sumnums[i-1]+nums[i]
        """
        :type nums: List[int]
        """
        

    def sumRange(self, left, right):
        # print(self.sumnums)
        # print(self.nums)
        return (self.sumnums[right]-self.sumnums[left] + self.nums[left])
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
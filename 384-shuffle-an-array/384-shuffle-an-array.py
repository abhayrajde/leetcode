class Solution(object):

    def __init__(self, nums):
        self.nums = nums
        """
        :type nums: List[int]
        """
        

    def reset(self):
        return self.nums
        """
        :rtype: List[int]
        """
        

    def shuffle(self):
        shuffle = self.nums[:]
        for i in range(len(shuffle)-1, -1, -1):
            index = random.randrange(0,i+1)
            shuffle[i],shuffle[index] = shuffle[index], shuffle[i]
        return shuffle
        """
        :rtype: List[int]
        """
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
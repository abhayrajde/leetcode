class Solution(object):
    def triangularSum(self, nums):
        #TC - O(N^2)
        while(len(nums)>1):
            for i in range(len(nums)-1):
                temp = nums[i] + nums[i+1]
                if(temp>9):
                    temp %= 10
                nums[i] = temp
            nums.pop()
        return(nums[0])
        """
        :type nums: List[int]
        :rtype: int
        """
        
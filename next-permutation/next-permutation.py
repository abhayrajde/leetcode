class Solution(object):
    def nextPermutation(self, nums):
        if(len(nums)<=2):
            return nums.reverse()
        i = len(nums)-1
        while(i>0 and nums[i] <= nums[i-1]):
            i-=1
        if(i == 0):
            return (nums.reverse())
            
        for j in range(len(nums)-1,i-1,-1):
            if(nums[j] > nums[i-1]):
                nums[j],nums[i-1] = nums[i-1],nums[j]
                break
        nums[i:] = reversed(nums[i:])
        return nums
            
        
        """
        for i in range(len(nums)-1,0,-1):
            if(nums[i]>nums[i-1]):
                nums[i],nums[i-1] = nums[i-1],nums[i]
                break
        else:
            nums.sort()
        """
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
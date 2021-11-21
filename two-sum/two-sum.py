class Solution(object):
    def twoSum(self, nums, target):    
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if(nums[i]+nums[j]==target):
                    return i,j
        """
        nums.sort()
        i = 0
        j = len(nums)-1
        while(i<j):
            
            if(nums[i]+nums[j]==target):
                return i,j
            
            if(nums[i]+nums[j]<target):
                i+=1
            
            if(nums[i]+nums[j]>target):
                j-=1
        """
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
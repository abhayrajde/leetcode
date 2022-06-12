class Solution(object):
    def twoSum(self, nums, target):    
        hm = {}
        for i in range(len(nums)):
            if((target - nums[i]) in hm):
                return(i,hm[target - nums[i]])
            else:
                hm[nums[i]] = i
        
                
                
        
        
        """
        #Brute Force
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if(nums[i]+nums[j]==target):
                    return i,j
        """
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
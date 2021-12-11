class Solution(object):
    def sortColors(self, nums):
        # this algorithm is the variation of dutch national flag algo
        low,mid = 0,0
        high = len(nums)-1
        
        while(mid<=high):
            if(nums[mid] == 0):
                nums[mid],nums[low] = nums[low],nums[mid]
                low+=1
                mid+=1
            elif(nums[mid] == 1):
                mid+=1
            elif(nums[mid] == 2):
                nums[high],nums[mid] = nums[mid],nums[high]
                high-=1
        return(nums)
                
                
                
        
        
        """ 
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
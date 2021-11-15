class Solution(object):
    def removeElement(self, nums, val):
        i = 0               # this pointer will keep track of proper sequence
        j = len(nums)-1
        count = 0
        while(i<=j):
            if(nums[i] != val):
                i+=1
                
                
            elif(nums[i] == val):
                nums[i],nums[j] = nums[j],nums[i]
                j-=1
        return(i)
                
        
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
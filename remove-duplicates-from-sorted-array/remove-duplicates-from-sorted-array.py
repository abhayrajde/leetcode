import copy
class Solution(object):
    def removeDuplicates(self, nums):
        i = 0
        j = 1
        while(j < len(nums)):
                
            if(nums[i] == nums[j]):
                j+=1
            
            elif(nums[i] != nums[j]):
                nums[i+1] = nums[j]
                i+=1
                j+=1
        return(i+1)
                
            
            
        
        """
        # expected output doesnt need the extra repeated terms, so getting this code wrong
        # initialize pointer to keep track of where the new unique character can be inserted
        p = 0
        uni = []  # here we will store all the unique values
        for i in range(len(nums)):
            if(i not in uni):
                uni.append(nums[i])
                temp = nums[i]
                nums[i] = nums[p]
                nums[p] = temp
                p+=1
        nums = uni
        return (p+1)
        """
        """
        :type nums: List[int]
        :rtype: int
        """
        
class Solution(object):
    def maxProduct(self, nums):
        cmax,cmin = 1,1
        max1 = max(nums)
        for i in range(len(nums)):
            
            if(nums[i] == 0):
                cmax,cmin = 1,1
            
            temp1 = cmax*nums[i]
            temp2 = cmin*nums[i]
            
            cmax = max(temp1,temp2,nums[i])
            cmin = min(temp1,temp2,nums[i])
            
            if(cmax > max1):
                max1 = cmax
        return(max1)
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        """
        currmax = 1
        currmin = 1
        max1 = max(nums)
        for i in range(len(nums)):
            if (nums[i] == 0):
                currmax, currmin = 1,1
            
            temp1 = currmax * nums[i]
            temp2 = currmin * nums[i]
            currmax = max(temp1, temp2, nums[i])
            currmin = min(temp1, temp2, nums[i])
            max1 = max(currmax, max1)
        return(max1)
        """
        # max1 = nums[0]
        # prod = 1
        # for i in range(len(nums)):
        #     prod = prod*nums[i]
        #     if(prod > max1):
        #         max1 = prod
        #     else:
        #         prod = 1
        # return(max1)
                
        """
        :type nums: List[int]
        :rtype: int
        """
        
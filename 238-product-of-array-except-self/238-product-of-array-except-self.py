class Solution(object):
    def productExceptSelf(self, nums):
        res = [1] * len(nums)
        
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for j in range(len(nums)-1,-1,-1):
            res[j] *= postfix
            postfix *= nums[j]
        return(res)
            
            
        # #Time Complexity - O(n^2) - not okay
        # l = len(nums)
        # op = [1]*l
        # for i in range(len(nums)):
        #     for j in range(len(op)):
        #         if(i!=j):
        #             op[j]*=nums[i]
        # return(op)
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
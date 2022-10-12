class Solution(object):
    def findMin(self, nums):
        # 
        start = 0
        end = len(nums)-1
        # mid = (start + end)//2
        res = nums[0]
        while end >= start:
            if nums[start] < nums[end]:
                res = min(res,nums[start])
                break
            
            mid = (start + end)//2
            res = min(res,nums[mid])
            
            if nums[mid] >= nums[start]:
                start = mid + 1
            
            else:
                end = mid - 1
        return res
            
            
            
                
        """
        :type nums: List[int]
        :rtype: int
        """
        
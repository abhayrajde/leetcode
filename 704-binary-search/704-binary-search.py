class Solution(object):
    def search(self, nums, target):
        low = 0
        high = len(nums)-1
        while(low <= high):
            mid = (high + low)//2
            if(target == nums[mid]):
                return(mid)
            
            if(target < nums[mid]):
                high = mid - 1
                # mid = (high + low // 2)
                
            else:
                low = mid + 1
                # mid = (high + low // 2)
        
        return(-1)
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
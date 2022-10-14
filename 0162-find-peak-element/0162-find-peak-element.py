class Solution(object):
    def findPeakElement(self, nums):
        l, r = 0, len(nums) - 1
        
        while(l<=r):
            mid = (l+r)//2
            
            #check if mid is peak
            if ((mid == 0 or nums[mid-1]<nums[mid]) and (mid == len(nums)-1 or nums[mid+1] < nums[mid])):
                # this mid is a peak so we return that
                return mid
            
            # if mid is not a peak, then we have 2 options
            # look to the left or the right
            # search the left
            elif(mid>0 and nums[mid-1] > nums[mid]):
                r = mid-1
            #search right
            elif(mid<len(nums)-1 and nums[mid+1] > nums[mid]):
                l = mid+1
            
        """
        :type nums: List[int]
        :rtype: int
        """
        
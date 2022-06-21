class Solution(object):
    def search(self, nums, target):
        l = 0
        r = len(nums)-1
        # m = (l+r)//2
        while(l<=r):
            m = (l+r)//2
            if(nums[m] == target):
                return(m)
            #if target in right ride of the mid
            if(nums[l]<=nums[m]):
                if(target<nums[l] or target>nums[m]):
                    l = m+1
                else:
                    r = m-1
            #If target in left side of the mid num
            else:
                if(target>nums[r] or target<nums[m]):
                    r = m-1
                else:
                    l = m+1
        return(-1)
                
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        